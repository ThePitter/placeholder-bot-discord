# imports
import bot_prefix
import bot_test_actions

# all major actions should go here. commands should be in all lowercase to support any case
actions = {
    "goodbye" : bot_test_actions.goodbye_response,
    "setprefix" : bot_prefix.change_prefix,
    "changeprefix" : bot_prefix.change_prefix,
}


# This manages checking for a command and running the response and actions if the command was run
async def manage_actions(message):
    for command in actions:
        if message.content.strip().lower().startswith(bot_prefix.prefix + command):
            await actions[command](message)
