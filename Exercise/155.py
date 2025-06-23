from parsers import convert

import FreeSimpleGUI as bk

label1 = bk.Text("Enter feet")
input1=bk.Input(key="feet")
label2 = bk.Text("Enter inches")
input2=bk.Input(key="inches")

convert_button=bk.Button("Convert")

output_label=bk.Text(key="output",text_color="Orange")

window =bk.Window("Convertor",
                  [[label1,input1],
                   [label2,input2],
                   [convert_button ,output_label]])
while True:
    event, values = window.read()
    feets=float(values["feet"])
    inches=float(values["inches"])
    meters=convert(feets,inches)
    window["output"].update(value=f"{meters} m", text_color="white")


window.close()