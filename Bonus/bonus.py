#Bonus_101
'''try:
    width=float(input("Enter the rec width:"))
    length =float(input("Enter rec len:"))

    if width==length:
        exit("That look like a square")
    area = width*length
    print(area)
except ValueError:
    print("please enter a number")'''

'''try:
    total_value=float(input("Enter total value:"))
    value =float(input("Enter value:"))
    per =value/total_value*100
    print(f"That is {per}%")
except ValueError:
    print("You need to enter a number. Run the program again.")  
except ZeroDivisionError:
    print("Your total value cannot be zero")'''

#Bonus_109
'''def get_avg():
    with open('file.txt', 'r') as file_local:
        data = file_local.readlines()

    values=data[1:]
    values=[float(i) for i in values]
    avg_local =sum(values)/len(values)
    return  avg_local


avg =get_avg()
print(avg)


def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = f"MAX:{max(grades)},Min:{min(grades)}"
    return maximum


print(get_max())'''

'''feet_inches=input("Enter height of kid in feet and inches: ")

f,i= parse(feet_inches)
print("fi",f,i)
result = convert(f, i)
if result < 1:
    print("Potti na koduku")
else:
    print("Ok you can go")'''
FREEZING_POINT=0
BOILING_POINT=100

def water_state(temperature):
    if temperature <=FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT <temperature <BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"

#result=water_state(float(input("temp")))
#print(result)



