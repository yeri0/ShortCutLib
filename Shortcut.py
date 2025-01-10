class Shortcut:
    __name = ""
    __description = ""
    __shortcut_string = ""

    def __init__(self,shortcut_name, shortcut_description, shortcut):
        self.__name = shortcut_name
        self.__description = shortcut_description
        self.__shortcut_string = shortcut

    def change_description(self, new_description):
        self.__description = new_description

    def change_shortcut(self, new_shortcut):
        self.__shortcut_string = new_shortcut

    def change_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_shortcut(self):
        return self.__shortcut_string
