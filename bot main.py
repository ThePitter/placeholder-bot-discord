# This is the main script for the bot. Run this one to start the bot, atleast that's how I think this works

import discord # view discord.py documents at https://discordpy.readthedocs.io
import bot_token
import bot_test_actions
import bot_prefix

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
    #if message.content.startswith("/Hello"):
    #    await message.channel.send('Hello There')
    await bot_test_actions.test_replies(message)



# This line must be last, it starts the bot :D
client.run(bot_token.bottoken)