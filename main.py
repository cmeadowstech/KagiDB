import requests
import os
import pprint
import json
import discord
from dotenv import load_dotenv
from discord import app_commands
import typing

load_dotenv()

pp = pprint.PrettyPrinter(indent=4)


def get_kagi_sum(article, summary_type):
    url = "https://kagi.com/mother/summary_labs"

    payload = {"summary_type": summary_type.lower(), "url": article}
    headers = {
        "Authorization": "GwDAbP3QUQU.gN_TrLK59kbRXNafxk8ddpUF0G_18ksWEKO6aMxuoNs",
        "Cookie": "kagi_session=GwDAbP3QUQU.gN_TrLK59kbRXNafxk8ddpUF0G_18ksWEKO6aMxuoNs",
    }

    response = requests.request("GET", url, headers=headers, params=payload)
    return json.loads((response.text))


# pp.pprint(kagi_sum('https://apnews.com/article/hmong-spiritual-new-year-shamanism-animism-e4bc9026b7840919d86e97d7d4fa1a77').json())

MY_GUILD = discord.Object(id=175799272976023563)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")


@client.tree.command(
    description="Usese Kagi's summarizer AI to summarize articles",
)
@app_commands.describe(
    url="URL of the article to summarize",
    summary_type="summary or takeaway (bullet points). Default = summary",
)
async def sum(
    interaction: discord.Interaction,
    url: str,
    summary_type: typing.Optional[str] = "summary",
):
    await interaction.response.defer()
    summary = get_kagi_sum(url, summary_type)
    await interaction.followup.send(
        f"Here's your summary for the article {url}:\n\n{summary['output_data']['markdown']}"
    )


client.run(os.getenv("TOKEN"))
