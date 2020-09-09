# This is the main script for the bot. Run this one to start the bot, atleast that's how I think this works

import discord # view discord.py documents at https://discordpy.readthedocs.io
import bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))



# This line must be last, it starts the bot
client.run(bot_token.bottoken)