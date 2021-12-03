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
    ITALICS = '\x1B[3m'


#FUNCTIONS
def menu_addEntry():
    "Home menu selection #1"
    homework = input(prompt("\nWhat is the homework? "))
    escaper(homework)
    subject = input(prompt("What subject is this homework from? "))
    escaper(subject)
    deadline = input(prompt("When is the deadline? "))
    escaper(deadline)
    notes = input(prompt("Notes(optional): "))
    escaper(notes)
    database.add_entry(homework, subject, deadline, notes)
    confirmation("\nAdd entry successful!")
    message_return_home()
    home_menu()

def menu_displayEntries(entries):
    "Home menu selection #2"
    for entry in entries:
        print(f"\nEntryID:        {entry[0]}\nHomework title: {entry[1]}\nSubject:        {entry[2]}\nDeadline:       {entry[3]}\nNotes:          {entry[4]}\nStatus:         {replace(entry[5])}\n")

def menu_editEntry():
    "Home menu selection #3"
    tester_list = ["homework", "subject", "deadline", "notes"]
    num_EE = input(prompt("\nEnter entry ID: "))
    escaper(num_EE)
    check_ifNum(num_EE)
    view_single_entry(num_EE)
    choose_entry = input(prompt("Edit name/date for homework, subject, deadline or notes? "))
    escaper(choose_entry)
    choose_entry = choose_entry.lower()

    if choose_entry in tester_list:
        new_name = input(prompt(f"\nEnter new name/date of {choose_entry}: "))
        database.update_entry(choose_entry, new_name, num_EE)
        confirmation("\nEdit success!")
    else:
        print(warning("\nInvalid input"))
        
    message_return_home()
    home_menu()

def menu_finish():
    "Home menu selection #4"
    num_F = input(prompt("\nEnter entry ID: "))
    view_single_entry(num_F)
    answer_F = input(txt_style.YELLOW + f"\nSet status of this homework entry as finished? Type in \"Yes\" to continue (Warning: this action can't be undone). . ." + txt_style.ENDC)
    if answer_F.lower() == "yes":
        database.finish_entry(num_F)
        confirmation("\nStatus set as FINISHED!")
    else:
        print(txt_style.ITALICS + txt_style.RED +"\n  Cancelled" + txt_style.ENDC)
    message_return_home()
    home_menu()

def menu_deleteEntry():
    "Home menu selection #5"
    num_DE = input(prompt("\nEnter ID of entry: "))
    escaper(num_DE)
    check_ifNum(num_DE)
    view_single_entry(num_DE)
    answer_DE = input(warning(f"\nDelete this homework entry? Type in \"Yes\" to continue. . . "))
    if answer_DE.lower() == "yes":
        database.delete_entry(num_DE)
        confirmation("\nDelete successful!")
    else:
        print(txt_style.ITALICS + txt_style.RED +"\n  Cancelled" + txt_style.ENDC)
    message_return_home()
    home_menu()

def menu_deleteAllEntries():
    "Home menu selection #6"
    answer_DAE = input(warning("\nAre you sure you want to delete all homework entries? Type in \"Yes\" to continue. . . "))
    if answer_DAE.lower() == "yes":
        database.delete_all_entries()
        confirmation("\nDeleted all entries!")
    else:
        print(txt_style.ITALICS + txt_style.RED +"\n  Cancelled" + txt_style.ENDC)
    message_return_home()
    home_menu()

def view_single_entry(num):
    "menu_editEntry(), menu_finish() and menu_deleteEntry() calls this function"
    single_row = database.get_single_entry(num)
    for entry in single_row:
        print(f"\nEntryID:        {entry[0]}\nHomework title: {entry[1]}\nSubject:        {entry[2]}\nDeadline:       {entry[3]}\nNotes:          {entry[4]}\nStatus:         {replace(entry[5])}\n")

def escaper(x):
    "Input tester: if the input is 'esc', cancel the operation"
    if x.lower() == "esc":
        print(txt_style.ITALICS + txt_style.RED +"\n  Cancelled" + txt_style.ENDC)
        message_return_home()
        home_menu()

def replace(status):
    "Replaces the value of a string"
    if status != "FINISHED":
        status = "Pending"
    elif status == "FINISHED":
        status = highlight(status)
    return status

def check_ifNum(x):
    "Input tester: checks if the input is a digit"
    if not x.isdigit():
        print(warning("\nInvalid input"))
        message_return_home()
        home_menu()

#Templates
def title(message):
    return print(txt_style.BOLD + txt_style.PURPLE + message + txt_style.ENDC)

def highlight(message):
    return txt_style.YELLOW + message + txt_style.ENDC

def header(message):
    return print(txt_style.BOLD + txt_style.BLUE + message + txt_style.ENDC)

def prompt(message):
    return txt_style.GREEN + message + txt_style.ENDC

def confirmation(message):
    return print(txt_style.BOLD + txt_style.YELLOW + message + txt_style.ENDC)

def warning(message):
    return txt_style.BOLD + txt_style.RED + message + txt_style.ENDC

def escape_info():
    return print(txt_style.PURPLE + "Tip: Type in 'esc' to cancel" + txt_style.ENDC)

def message_return_home():
    a = input(txt_style.CYAN + "Press ENTER to return go back to menu. . ." + txt_style.ENDC)

#also the main function
def home_menu():
    title("""

                    █░█ █▀█ █▀▄▀█ █▀▀ █░█░█ █▀█ █▀█ █▄▀   █▀█ █▀█ █▀▀ ▄▀█ █▄░█ █ ▀█ █▀▀ █▀█
                    █▀█ █▄█ █░▀░█ ██▄ ▀▄▀▄▀ █▄█ █▀▄ █░█   █▄█ █▀▄ █▄█ █▀█ █░▀█ █ █▄ ██▄ █▀▄
    """)

    header(f"\n\nPlease select a number from one of the following options:")

    prompt_message = "\nYour Selection: "
    menu = f"""
    {highlight("1")}: Add new homework entry                                           Homework entry example:
    {highlight("2")}: View homework entries                                            1                        <--  Entry ID
    {highlight("3")}: Edit homework entry                                              Make a simple program    <--  Homework
    {highlight("4")}: Set homework's status as finished                                Programming              <--  Subject
    {highlight("5")}: Delete a homework entry                                          Jan 1, 2021              <--  Deadline
    {highlight("6")}: Delete all homework entries
    {highlight("7")}: Exit
    """

    user_input = input(menu + prompt(prompt_message))

    if user_input == "1":
        header("\n-------------Add new homework entry-------------")
        escape_info()
        menu_addEntry()
    elif user_input == "2":
        header("\n-------------Here are your homework/s-------------\n")
        menu_displayEntries(database.get_entries())
        message_return_home()
        home_menu()
    elif user_input == "3":
        header("\n-------------Edit a homework entry-------------")
        escape_info()
        menu_displayEntries(database.get_entries())
        menu_editEntry()
    elif user_input == "4":
        header("\n-------------Set homework's status as finished-------------")
        escape_info()
        menu_displayEntries(database.get_entries())
        menu_finish()
    elif user_input == "5":
        header("\n-------------Delete a homework entry-------------")
        escape_info()
        menu_displayEntries(database.get_entries())
        menu_deleteEntry()
    elif user_input == "6":
        header("\n-------------Delete all homework entries-------------")
        menu_deleteAllEntries()
    elif user_input == "7":
        sys.exit()
    else:
        print(warning("\nInvalid input"))
        message_return_home()
        home_menu()



#START OF PROGRAM
database.create_table()

home_menu()

database.close()