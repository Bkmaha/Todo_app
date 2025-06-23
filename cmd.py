from function import get_todos,write_todos
#import function
import time

''' To use function in different file follow bellow syntax
    function.get_todos() 
    '''
now =time.strftime("%b %d,%Y %H:%M:%S")
print("It is",now)
while True:
    user_action=input("type add,show,edit,complete or exit: ")
    user_action=user_action.strip()

    if  user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos=get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        new_todos=[]
        todos = get_todos()
        for item in todos:
            new_item=item.strip('\n')
            new_todos.append(new_item)
        for index,item in enumerate(new_todos):
            row=f"{index+1}-{item.capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            number=number-1
            todos=get_todos()

            new_todos = input("Enter new todo: ")
            todos[number]=new_todos + '\n'
            write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[8:])
            todos= get_todos()
            index = number-1
            todo_to_remove =todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            message =f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("command is Not Valid")
print("Bye")