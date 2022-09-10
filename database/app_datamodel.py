"""OK this is a code file that helps us create the database model"""
from dataclasses import dataclass


class Person:
    """It stores the information of n person"""
    id: int
    name: str
    surname: str


class Account:
    """It stores the information of their account"""
    account_number: int
    account_balance: int


class Attendence:
    """Store when they sign in for work"""
    timestamp: int
    id: int


DATABSE_TABLES:list[object] = [Person, Account, Attendence]

def get_model()->dict:
    """Returns the model
    {'Person': {'id': <class 'int'>, 'name': <class 'str'>, 'surname': <class 'str'>},
     'Account': {'account_number': <class 'int'>, 'account_balance': <class 'int'>},
     'Attendence': {'timestamp': <class 'int'>, 'id': <class 'int'>}}"""
    model:dict = {} # Dictionaries {key : value} - Good way to store data
    for table in DATABSE_TABLES: # Each class is a Table 
        table_name = table().__class__.__name__ # Programatically getting the table name for the class name
        columns = table.__annotations__ # Getting the column names 
        model[table_name] = columns # creating the dictionary entry
    return model

print(get_model())