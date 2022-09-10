"""Vscode file creates the database functions and helps us create the database read to the database set up in the database and etceter"""
import sqlite3
import os

def connect_database(database_location)->sqlite3.Connection|bool:
    """Conencts to the database
    ## Will return the database object if the location exist
    ## Otherwise return False"""
    if os.path.exists(database_location):
        connect = sqlite3.connect(database_location)
        return connect
    return False

def create_datebase(database_loaction:str)->sqlite3.Connection:
    """Creates database"""
    return sqlite3.connect(database_loaction)


def create_tables(table_dictionary:dict, database_cursor:sqlite3.Cursor=None):
    """Creates tables in the databse"""
    if database_cursor is None:
        database_cursor = sqlite3.connect("Test.db").cursor()      
    table_names = table_dictionary.keys()
    for table in table_names:
        columns = table_dictionary[table].keys()
        colum_str = "("
        for column in columns:
            data_type_class = table_dictionary[table][column]
            data_type = ""
            if data_type_class is str:
                data_type = "text"
            elif data_type_class is int:
                data_type = "integer"
            else:
                data_type = "text"
        colum_str += ")"
        script = f"CREATE TABLE IF NOT EXISTS {table}({colum_str})"
        print(script)
    return 


def read_date():
    """Reads data form database"""
    return

def insert_data():
    """Inserts data in database"""
    return

def update_data():
    """Updatse data in the database"""
    return