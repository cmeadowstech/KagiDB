# Discord bot integrating Kagi's summarization AI

![image](https://github.com/cmeadowstech/KagiDB/assets/30964870/a9ecdfa5-8604-4896-a5e2-3fdd3357c192)

## Install requirements

First, install the pip requirements.

```
pip install -r requirements.txt
```

## Set authentication token

Requires a Kagi session token, which can be found under Settings -> Account -> Session Link. The token comes after ?token=

Then, create a .env file with the following:

```
DISCORD_TOKEN=<discord bot token>
KAGI_TOKEN=<kagi token>
```

## Discord Bot

You will also need to create a Discord Bot: https://discordpy.readthedocs.io/en/stable/discord.html
- I believe this is a bit old and Discord now requires a redirect url. By default it should be https://discordapp.com/oauth2/authorize?&client_id=[CLIENTID]&scope=bot
  - Replace [CLIENTID] with the client id of your bot
 
## Usage

Currently there are two commands:

```
/sum url:[required] summary_type:[default = summary, optional(summary, takeaway)]
```
```
/qa query:[required]
```
