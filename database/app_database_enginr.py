"""Has the code that drives the database"""
import database.app_datamodel as database_model
import database.app_database as database_connect

DATABASE_LOCATION = "./app_database.db"



def setup_app_database(database):
    """Sets up the database"""
    model:dict = database_model.get_model()

    return

def initialise_database(database_location=None):
    """Inistialises the database"""
    if database_location is None:
        database_location = DATABASE_LOCATION
    connect_database = database_connect.connect_database(database_location)
    if connect_database: return connect_database
    created_new_database = database_connect.create_datebase(database_location)
    return created_new_database

def get_database(database_location=None):
    """Set up the database for use"""
    if database_location is None:
        database_location = DATABASE_LOCATION
    app_database = initialise_database(database_location)
    setup_app_database(app_database)
    return app_database


def create_record(table, record):
    """Creates record in table"""
    return

def load_record(table, term):
    """Searches the table and term"""
    return

def insert_attendence(timestamp, person_id):
    """Creates the record of the attendence"""
    return

def get_person(id, name, surname):
    """Gets the person's information"""
    return

def get_account(account_number, account_balance):
    """Gets the person's account details"""
    return

def insert_person():
    return
