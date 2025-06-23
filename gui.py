import function
import FreeSimpleGUI as sg

from function import get_todos

label=sg.Text("Type in a to-do")
input_box=sg.InputText("Enter todo")
add_button=sg.Button("Add")

window=sg.Window('My To-Do App',layout=[[label],[input_box,add_button]])
window.read()

window.close()

