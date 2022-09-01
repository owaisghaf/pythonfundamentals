
print("Welcome to find out if you are smart or dumb, "
      "This application will calculate the average percentage mark you have achieved across Maths, Chemistry and Physics.")

print(50*'-')

Maths_mark = int(input("Please enter your mathematics mark (out of 100) "))
print(f"Your mathematics mark is {Maths_mark}%")

print(50*'-')

""" 
if Maths_mark > 100 or Maths_mark < 0:
    Maths_mark = int(input(f"You have entered the wrong mark, Please enter the correct mark"))

NEED TO FIND A FIX FOR THE ABOVE - THIS WILL STOP YOU INPUTTING A VALUE OUTSIDE OF CERTAIN CONDITIONS AND NOT
PROCEED UNTIL THOSE CONDITIONS HAVE BEEN MET.
"""

Chemistry_mark = int(input("Please enter your Chemistry mark (out of 100)"))
print(f"Your Chemistry mark is {Chemistry_mark}%")

print(50*'-')

Physics_mark = int(input("Please enter your Physics mark (out of 100)"))
print(f"Your Physics mark is {Physics_mark}%")

print(50*'-')

Total_mark = Maths_mark + Chemistry_mark + Physics_mark
print(f"Your total overall mark is {Total_mark}")

print(50*'-')

Percentage_mark = int(Total_mark / 3)
print(f"Your overall percentage mark is {Percentage_mark}")

print(50*'-')

if 100 >= Percentage_mark >= 70:
    print('Congrats you smart arse, you got an A!')
elif 70 > Percentage_mark >= 60:
    print('Congrats you are fairly smart, you got a B!')
elif 60 > Percentage_mark >= 50:
    print('meh try harder, you got a C!')
elif 50 > Percentage_mark >= 40:
    print('you are quite dumb, resit for you, you got a D!')
else:
    print('you are STUPID, you Failed!')
