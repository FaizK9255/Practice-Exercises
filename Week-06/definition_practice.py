# 00 create a definition for compare numbers
# 01 ask for an input from user for two different numbers
# 02 have a function that finds the greater of the 2 numbers given
# 03 then use a print statement to display the greater number
# 04 call back to the definition function

def compare_numbers(num1, num2):
    if num1>num2:
        print(f'{num1} is greater than {num2}')
    elif num2>num1:
        print(f'{num2} is greater than {num1}')
    else:
        print("Both numbers are equal.")

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

compare_numbers(number1, number2)
