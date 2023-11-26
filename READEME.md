# Discord bot integrating Kagi's summarization AI

## Install requirements

First, install the pip requirements.

```
pip install -r requirements.txt
```

## Set authentication token

Requires a Kagi session token, which can be found under Settings -> Account -> Session Link. The token comes after ?token=

Then, create a .env file with the following:

```
TOKEN=<Kagi token>
```

## Discord Bot

You will also need to create a Discord Bot: https://discordpy.readthedocs.io/en/stable/discord.html
- I believe this is a bit old and Discord now requires a redirect url. By default it should be https://discordapp.com/oauth2/authorize?&client_id=[CLIENTID]&scope=bot
  - Replace [CLIENTID] with the client id of your bot

