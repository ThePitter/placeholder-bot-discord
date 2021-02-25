# imports
import bot_prefix
import bot_misc_actions
import question
from action import shared

# all major actions should go here. commands should be in all lowercase to support any case
'''
actions = {
    "goodbye" : bot_misc_actions.goodbye_response,
    "setprefix" : bot_prefix.change_prefix,
    "changeprefix" : bot_prefix.change_prefix,
    "testpast" : bot_misc_actions.test_past_messages,
    "hello" : bot_misc_actions.hello_response,
    "question" : question.question_input,
}
'''


# This manages checking for a command and running the response and actions if the command was run
async def manage_actions(message):
    global actions

    for command in shared.actions:
        if message.content.strip().lower().startswith(bot_prefix.prefix + command):
            await shared.actions[command](message)
    
    if message.content.strip().lower().startswith(bot_prefix.prefix + "help"):
        content = message.content.split(" ")
        if len(content) > 1:
            if content[1] in shared.actions:
                try:
                    await message.channel.send(shared.actions[content[1]].description)
                except:
                    await message.channel.send("There's no specific help on this command at the moment.")
            else:
                await message.channel.send("That command doesn't exist. Try {}help for a list of commands.", bot_prefix.prefix)
        else:
            summary = "Available actions:\n"
            for a in shared.actions:
                summary += a + "\n"
            await message.channel.send(summary)