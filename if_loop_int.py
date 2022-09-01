"""
- if loop to compare operator input to set values.
- Cannot compare a string to an integer
- Simple Calculator
"""
import random

option = input("please use the +, -, *, / symbol to indicate what operation to conduct ")
A = int(input('enter a number between 1 and 10 '))
B = int(input('enter a number between 1 and 10 '))

if option == '+':
    Answer = A + B
    print(f"The sum of the 1st and 2nd numbers = {Answer}")
elif option == '-':
    Answer = A - B
    print(f"The subtraction of the 1st and 2nd numbers = {Answer}")
elif option == '*':
    Answer = A * B
    print(f"The multiplication of the 1st and 2nd numbers = {Answer}")
elif option == '/':
    Answer = A / B
    print(f"The Division of the 1st and 2nd numbers = {Answer}")
else:
    input(f"please insert a numerical operator")

print(50*'_')

D = random.randint(1,10)
E = random.randint(1,10)
Answer= D * E # replace with A*B

# concatenates a string and an integer by converting the integer into a string. Need a + after every seperation
C = int(input("what is" + str(D) + "x" + str(E) + "? "))

if C == Answer:
    print('You are correct!')
elif C>Answer:
    print('Too big! try again')
else:
    print('Too small, try again')

option2 = input("do you want to know the answer (yes/no)?")
if option2 == yes:
    print('The answer is ' + str(Answer))
elif option2 == no:
    print('Ok, please try again')
else:
    print('enter a valid answer')