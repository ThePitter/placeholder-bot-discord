# imports
import bot_prefix

# all major actions should go here. commands should be in all lowercase to support any case
actions = {
    "goodbye" : goodbye_response,
    "setprefix" : bot_prefix.change_prefix,
    "changeprefix" : bot_prefix.change_prefix,
}


# This manages checking for a command and running the response and actions if the command was run
async def manage_actions(message):
    for command in actions:
        if message.content.strip().lower().startswith(bot_prefix.prefix + actions):
            await actions[command](message)


# add the response/action for a command here, or i guess it could be an import from somewhere else
async def goodbye_response(message):
    await message.channel.send("Hmm... I can't leave")