# imports
import bot_prefix
import bot_misc_actions

# all major actions should go here. commands should be in all lowercase to support any case
actions = {
    "goodbye" : bot_misc_actions.goodbye_response,
    "setprefix" : bot_prefix.change_prefix,
    "changeprefix" : bot_prefix.change_prefix,
    "testpast" : bot_misc_actions.test_past_messages,
    "hello" : bot_misc_actions.hello_response,
}


# This manages checking for a command and running the response and actions if the command was run
async def manage_actions(message):
    global actions

    for command in actions:
        if message.content.strip().lower().startswith(bot_prefix.prefix + command):
            await actions[command](message)
    
    if message.content.strip().lower().startswith(bot_prefix.prefix + "help"):
        content = message.content.split(" ")
        if len(content) > 1:
            await message.channel.send("There's no specific help on functions at the moment.")
        else:
            summary = "Available actions:\n"
            for a in actions:
                summary += a + "\n"
            await message.channel.send(summary)
