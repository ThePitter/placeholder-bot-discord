import discord
import bot_prefix

async def test_replies(message, client):
    if message.content.begins_with("{bot_prefix.prefix}Hello"):
        await message.channel.send('Hello There')