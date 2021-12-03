import sqlite3
from sqlite3.dbapi2 import Cursor


connection = sqlite3.connect("data.db")


def create_table():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS homework_entries (entryID INTEGER PRIMARY KEY, homework TEXT, subject TEXT, deadline TEXT, notes TEXT)")
    connection.commit()

def add_entry(entry_homework, entry_subject, entry_deadline, entry_notes):
    connection.execute(
        f"INSERT INTO homework_entries(homework, subject, deadline, notes) VALUES('{entry_homework}', '{entry_subject}', '{entry_deadline}', '{entry_notes}')")
    connection.commit()

def get_entries():
    cursor = connection.cursor()
    return cursor.execute("SELECT * FROM homework_entries")

def get_single_entry(entry_entryID):
    cursor = connection.cursor()
    return cursor.execute(
        f"SELECT * FROM homework_entries WHERE entryID = '{entry_entryID}'")

def update_entry(entry_chosen, new_entryName, entry_entryID):
    cursor = connection.cursor()
    cursor.execute(
        f"UPDATE homework_entries SET '{entry_chosen}' = '{new_entryName}' WHERE entryID = '{entry_entryID}'")
    connection.commit()

def delete_entry(entry_entryID):
    cursor = connection.cursor()
    cursor.execute(
        f"DELETE FROM homework_entries WHERE entryID = '{entry_entryID}'")
    connection.commit()

def delete_all_entries():
    cursor = connection.cursor()
    cursor.execute(
        f"DELETE FROM homework_entries")
    connection.commit()

def close():
    connection.close()