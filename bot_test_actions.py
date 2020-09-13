import discord
import bot_prefix

async def test_replies(message):
    if message.content.startswith("/Hello"):
        await message.channel.send('Hello There')