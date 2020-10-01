import discord
import bot_prefix

async def test_past_messages(message):
    messages = await message.channel.history(limit=100).flatten()

    command_count = 0
    for msg in messages:
        if msg.content.startswith(bot_prefix.prefix):
            command_count += 1
    
    await message.channel.send("There have been " + str(command_count) + " previous commands in the past 100 messages.")


async def goodbye_response(message):
    await message.channel.send("Hmm... I can't leave")

async def hello_response(message):
    await message.channel.send("Hello there :D")


