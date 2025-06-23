'''
password= input("enter New password:")
result ={}
if len(password)>=8:
    result["len"]=True
else:
    result["len"]=False
digit=False
for i in password:
    if i.isdigit():
        digit=True
result["digits"]=digit
upper=False
for i in password:
    if i.isupper():
        upper=True
result["upper_Case"]=upper
print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")


def square_number():
    number = 5
    result = pow(number, 2)
    return result


num = square_number()
print(num)'''

from Exercise.parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)

