import discord
import bot_prefix
from action import action

@action("testpast")
async def test_past_messages(message):
    messages = await message.channel.history(limit=100).flatten()

    command_count = 0
    for msg in messages:
        if msg.content.startswith(bot_prefix.prefix):
            command_count += 1
    
    await message.channel.send("There have been " + str(command_count) + " previous commands in the past 100 messages.")

@action("goodbye", description = "Replies with a message")
async def goodbye_response(message):
    await message.channel.send("Hmm... I can't leave")

@action("hello", description = "Replies with a message")
async def hello_response(message):
    await message.channel.send("Hello there :D")


