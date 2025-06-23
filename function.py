#FILEPATH="new.txt"

def get_todos():
    with open('new.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local
def write_todos(todos_local,filepath ="new.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)