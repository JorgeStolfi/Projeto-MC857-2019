#This class is used to simulate the behavior of a database reference
class DatabaseReference:
    def __init__(self, dbname, username, password):
        self.__dbname = dbname
        self.__username = username
        self.__password = password

    def connect(self):
        '''
        It will always connect
        '''
        return True

    def execute_query(self, query):
        console.log("This is a query response")
        return

#Connect to dabase
def connect_to_users_database(database_name, user_name, password):
    '''
    Tries to connect to database
    '''

    database_reference = DatabaseReference("dbname", "user", "pass")
    database_reference.connect()
    return database_reference

def create_user(db_reference, name, age, email, password, address, gender, phone_number):
    '''
    Creates a new user
    '''

    console.log(f"User {name} created")
    return True

def retrieve_user_by_id(db_reference, id):
    '''
    Retrieve user by id
    '''
    console.log(f"User {id} retrieved")
    return True

def retrieve_user_by_email(db_reference, email):
    '''
    Retrieve user by email
    '''
    console.log(f"User {email} retrieved")
    return True

def update_user(db_reference, user_id, updates):
    '''
    Update user with the content of updates parameters.
    The updates parameter must be a list of tuples in which the first element of each tuple is the field name and the second element is the new field value.
    Ex: updates = [("name", "Victor"), ("age", 30)]
    '''
    console.log(f"User {user_id} updated")
    return True

def delete_user(db_reference, user_id):
    '''
    Delete user by id
    '''
    console.log(f"User {user_id} deleted")
    return True

def execute_custom_query(db_reference, sql_query):
    '''
    Executes custom SQL query
    '''
    console.log(f"Custom query {sql_query} executed")
    return True
