import discord
import bot_prefix

async def test_replies(message):
    if message.content.strip().startswith(bot_prefix.prefix + "Hello"):
        await message.channel.send('Hello There')