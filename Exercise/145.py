import  random
from os import urandom

Low_input=int(input("Enter the low limit of whole number"))
High_Input=int(input("Enter the High limit of whole number"))

number=random.randint(Low_input,High_Input)
print(number)