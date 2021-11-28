import sqlite3
from sqlite3.dbapi2 import Cursor


connection = sqlite3.connect("data.db")


def create_table():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (entryID INTEGER PRIMARY KEY, content TEXT, date TEXT)")
    connection.commit()


def close():
    connection.close()


def add_entry(entry_content, entry_date):
    connection.execute(
        f"INSERT INTO entries(content, date) VALUES('{entry_content}', '{entry_date}')")
    connection.commit()

def get_entries():
    cursor = connection.cursor()
    return cursor.execute("SELECT * FROM entries")

def delete_entry(entry_entryID):
    cursor = connection.cursor()
    cursor.execute(
        f"DELETE FROM entries WHERE entryID = '{entry_entryID}'")

def delete_entry():
    cursor = connection.cursor()
    cursor.execute(
        f"DELETE FROM entries")