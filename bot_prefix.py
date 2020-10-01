
# ALL STATEMENTS THAT REFER TO A COMMAND SHOULD IMPORT AND USE THIS unless requiring something else
prefix = '#'

# Future code to manage changing said prefix and more goes here
async def change_prefix(message):
    global prefix
    content = message.content.split(" ")
    if len(content) > 1:
        prefix = content[1]
        await message.channel.send("Prefix changed to: " + prefix)
    else:
        await message.channel.send("The current prefix is: " + prefix)
    