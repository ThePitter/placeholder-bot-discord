# Manages questions.

import discord
import random
import bot_prefix

async def question_input(message): # manages new questions
    text = message.content[9:].strip()
    await message.delete()
    id = random.randrange(start=0, stop=9999)
    text = "**" + bot_prefix.prefix + "q{:0>4}** " + text
    await message.channel.send(text.format(id))




async def answer_input(message): # manages answers to questions
    return