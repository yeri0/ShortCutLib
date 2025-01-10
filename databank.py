from Shortcut import Shortcut

def add_shortcut(Shortcut):
    try:
        with open("shortcuts.txt", "a") as f:
            f.write(Shortcut.get_name() + " " + Shortcut.get_description() + " " + Shortcut.get_shortcut() + "\n")
            print("Successfully appended to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_shortcut(Shortcut):
    pass

def clear_data_bank():
    with open("shortcuts.txt", "w") as f:
        f.close()

# Call the function to test it
test_object = Shortcut("1.", "Doesnt Do Anything", "Windows + R")
add_shortcut(test_object)
#clear_data_bank()