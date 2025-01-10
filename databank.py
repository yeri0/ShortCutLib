import system

def add_shortcut(Shortcut):
    try:
        with open("shortcuts.txt", "a") as f:
            f.write("test\n")
            print("Successfully appended to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_shortcut():
    pass

# Call the function to test it
add_shortcut()