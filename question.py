# Manages questions.

import discord
import random
import bot_prefix
import re # Regex functions, used to find if a string matches a pattern and such

async def question_input(message): # manages new questions
    text = message.content[9:].strip()
    await message.delete()
    id = random.randrange(start=0, stop=9999)
    text = "**" + bot_prefix.prefix + "q{:0>4}** " + text
    await message.channel.send(text.format(id))

async def get_past_questions(channel): # Returns questions from the past 500 messages in the provided channel. The questions are message objects.
    past = await channel.history(limit=500).flatten()
    question_messages = []
    for message in past:
        if re.search(bot_prefix.prefix + "q([0-9]{4})", message.content): #Finds a result if the tag matches a question with ID tag.
            question_messages.append(message)
    return question_messages

async def get_past_question(channel, question_id): # Returns question with specified id. Not to be confused with the plural questions function. Returns as message object or nothing.
    questions = await get_past_questions(channel)
    for q in questions:
        idx = q.content.find(str(question_id))
        if idx >= 2 and q.content[idx-2:idx] == bot_prefix.prefix + "q":
            return q

async def answer_input(message): # manages answers to questions
    # finds the #a0000 (prefix + a + four digit number) pattern and gets the specified message
    # if no message is found, reply back that that message is either out of range or non existent.
    # if the message is found, add the answer onto the question message and mark the message as pending verification

    return