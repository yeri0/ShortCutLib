from Shortcut import Shortcut

shortcutlist = []
size_shortcutlist = 0

def add_shortcut(shortcut: Shortcut):
    shortcutlist.append(shortcut)

def delete_shortcut(shortcut):
    if shortcut in shortcutlist:
        shortcutlist.remove(shortcut)
        return 1
    else:
        return 0

def change_name(shortcut: Shortcut, new_name):
    try:
        index = shortcutlist.index(shortcut)
        chosen = shortcutlist[index]
        chosen.change_name(new_name)

        return f"{new_name}"
    except ValueError:
        return "Not found"

def change_description(shortcut: Shortcut, new_description):
    try:
        index = shortcutlist.index(shortcut)
        chosen = shortcutlist[index]
        chosen.change_name(new_description)

        return f"{new_description}"
    except ValueError:
        return "Not found"

def search(shortcut: Shortcut):
    if shortcut in shortcutlist:
        return shortcut
    else:
        return 0
