# This is the main script for the bot. Run this one to start the bot, atleast that's how I think this works

import discord # view discord.py documents at https://discordpy.readthedocs.io
import bot_token
import bot_misc_actions
import bot_prefix
import bot_actions

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    #This statement is used to prevent an infinite loop activating any time the bot sends a message
    #   and attempts to read it's own message
    if message.author == client.user:
        return
    
    print(message.content)

    # Main code management for messages
    await bot_actions.manage_actions(message)



# This line must be last, it starts the bot :D
client.run(bot_token.bottoken)