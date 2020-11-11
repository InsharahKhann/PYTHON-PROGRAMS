     # ROLL NO. 008
'''
Write a Python program to check whether a
number is completely divisible by another
number. Accept two integer values form
the user. (HINT: %)'
'''

number1 = int(input ("the first number is: "))
number2 = int(input ("the second number is: "))

if (number1 % number2 == 0):
    print (number2, "is divisible by",number1)
