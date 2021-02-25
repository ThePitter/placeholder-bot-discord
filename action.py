class action_list:
    actions = {}

shared = action_list()

def action(command, description = "No description provided"):
    def wrapper(f):
        f.description = description
        shared.actions[command.lower()] = f
        return f
    return wrapper

