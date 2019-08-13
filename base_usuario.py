# Funções para gerenciar o banco de usuários.

# Implementação desta interface:


#Funções exportadas desta interface:
import base_usuario_IMP

#Connect to dabase
def connect_to_users_database(database_name, user_name, password):
    '''
    Tries to connect to database_name
    '''
    database_reference = base_usuario_IMP.connect_to_users_database(database_name, user_name, password)

    if database_reference is None:
        console.log("Error Trying to connect to database")
    return database_reference

def create_user(db_reference, name, age, email, password, address, gender, phone_number):
    '''
    Creates a new user
    '''
    return base_usuario_IMP.create_user(name, age, email, password, address, gender, phone_number)

def retrieve_user_by_id(db_reference, id):
    '''
    Retrieve user by id
    '''
    return base_usuario_IMP.retrieve_user_by_id(id)

def retrieve_user_by_email(db_reference, email):
    '''
    Retrieve user by email
    '''
    return base_usuario_IMP.retrieve_user_by_email(email)

def update_user(db_reference, user_id, updates):
    '''
    Update user with the content of updates parameters.
    The updates parameter must be a list of tuples in which the first element of each tuple is the field name and the second element is the new field value.
    Ex: updates = [("name", "Victor"), ("age", 30)]
    '''
    return base_usuario_IMP.retrieve_user_by_email(user_id, updates)

def delete_user(db_reference, user_id):
    '''
    Delete user by id
    '''
    return base_usuario_IMP.delete_user(user_id)

def execute_custom_query(db_reference, sql_query):
    '''
    Executes custom SQL query
    '''
    return base_usuario_IMP.execute_custom_query(sql_query)
