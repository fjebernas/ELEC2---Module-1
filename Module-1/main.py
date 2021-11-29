from os import system
import database
import sys

#CREATE CLASS FOR FONT COLORS AND STYLES
class txt_style:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALICS = '\x1B[3m'

#FUNCTIONS
def prompt_user_add_entry():
    header("\n----------Add an entry----------\n")
    entry_homework = input(prompt("What is the homework? "))
    entry_subject = input(prompt("What subject is this homework from? "))
    entry_deadline = input(prompt("When is the deadline? "))
    database.add_entry(entry_homework, entry_subject, entry_deadline)
    confirmation("\nAdd entry successful!")
    message_return_home()
    home_menu()

def display_entries(homework_entries):
    header("\n----------Here are your entries----------")
    for entry in homework_entries:
        print(f"\n{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n")
    message_return_home()
    home_menu()

def prompt_user_delete_entry():
    header("\n----------Delete an entry----------\n")
    entry_entryID = input("Enter ID of entry: ")
    answer = input(txt_style.BOLD + txt_style.RED + "\nDelete entry with the ID of " + entry_entryID + "? Type in \"Yes\" to continue. . . " + txt_style.ENDC)
    if answer.lower() == "yes":
        database.delete_entry(entry_entryID)
        confirmation("\nDelete successful!")
    message_return_home()
    home_menu()

def prompt_user_delete_all():
    header("\n----------Delete all entries----------")
    answer = input(txt_style.BOLD + txt_style.RED + "\nAre you sure you want to delete all entries? Type in \"Yes\" to continue. . . " + txt_style.ENDC)
    if answer.lower() == "yes":
        database.delete_all_entries()
        confirmation("\nDeleted all entries!")
    message_return_home()
    home_menu()

def title(message):
    return print(txt_style.BOLD + txt_style.PURPLE + message + txt_style.ENDC)

def sub_title(message):
    return print(txt_style.ITALICS + txt_style.BLUE + message + txt_style.ENDC)

def header(message):
    return print(txt_style.BOLD + txt_style.CYAN + message + txt_style.ENDC)

def prompt(message):
    return txt_style.GREEN + message + txt_style.ENDC

def confirmation(message):
    return print(txt_style.BOLD + txt_style.YELLOW + message + txt_style.ENDC)

def warning(message):
    return print(txt_style.BOLD + txt_style.RED + message + txt_style.ENDC)

def message_return_home():
    a = input("Press ENTER to return go back to menu. . .")

def home_menu():
    title("\n\n                  Welcome to the HOMEWORK ORGANIZER!")
    sub_title("                    never miss an assignment again\n\n")
    header("Please select one of the following options:")

    user_input = input(menu + prompt(prompt_message))

    if user_input == "1":
        prompt_user_add_entry()
    elif user_input == "2":
        display_entries(database.get_entries())
    elif user_input == "3":
        prompt_user_delete_entry()
    elif user_input == "4":
        prompt_user_delete_all()
    elif user_input == "5":
        sys.exit()
    else:
        warning("Invalid input")
        home_menu()

#VARIABLES
prompt_message = "\nYour Selection: "
menu = """
1. Add new homework entry.
2. View homework entries.
3. Delete a homework entry.
4. Delete all homework entries.
5. Exit.
"""


#START OF PROGRAM
database.create_table()

home_menu()

database.close()
