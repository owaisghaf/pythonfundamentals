import random

# This is how to do a single line comment

"""

this is how to do a multi line comment

"""

print(50 * '_')

# integer
A = 10
# float
B = 10.5
# string
C = 'my arse'
# boolean
D = False

print(50 * '_')

# prints the type of each of those variables
print(type(A))
print(type(B))
print(type(C))
print(type(D))

print(A, B, C, D)
print(type(A), type(B), type(C), type(D))

print(50 * '_')

# returns whether a statement is true of false
a = 5
b = 5
c = a is b
print(c)

print(50 * '_')

# assigning a True/False condition to a statement
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")  # concatenates strings
print("Statement:", name, "barks.", bark)  # the dog barking is TRUE as bark = True
print("Statement:", name, "tweets.", tweet)  # the dog tweeting is FALSE as Tweet = False

print(50 * "_")

quote_from_trek = """The line, "Beam me up scotty, was never used in Star Trek"
I'm sure you will find that this is an interesting fact"""

print(quote_from_trek)

print(50 * "_")

string_example = "I\'m going to the shops"  # \ignores the character after and turns to a string

print(string_example)

print(50 * "_")

first = 'fred'
name = first + ' ' 'blogs'

print(name)

print(50 * "_")

HP = 'my name is owais ghafoor'

print('the length of this string is = ', len(HP))
# returns length of the string/statement

print('this element in this string is = ', HP[-9])
# returns a specific value/character from a specific point in the string

print(50 * "_")

# Separating a string into a list and returning a specific value/string from a specific point in that split string
string_b = "Derrick,Matt,Jessica"
print(string_b)
string_c = string_b.split(",")
print("if we split the above into separate elements, it becomes ", string_c)
print("number 0 on the list is", string_c[0], ", number 1 on the list is", string_c[1],
      "and number 2 on the list is", string_c[2])

print(50 * "_")

# normal strings vs f string
names = ["luke", "leia", "han", "bumble", "p100D"]
print("the names are", names, "in the correct order and printed as a standard string")
print(f"the names are {names} in the correct order and printed as an f string")
print(f"the 3rd name is {names[2]}")

print(50 * "_")

# printing a string backwards - slicing
name = "Owais Ghafoor"
print(name[1::10].upper())

print(50 * "_")

# Integers and floats

""" 
n1 = int(input("enter a number between 1 and 10 "))
n2 = float(input("enter a number between 1 and 10 "))
n3 = n1 + n2
print(n3)
back_to_integer = int(n3) # rounds number down back into integer
print(back_to_integer)
"""

print(50*'_')

# Complex Numbers

n4 = 5+5j

print(f"this is a complex number {n4}")

print(50*'_')

# finding values/characters within a string

Owais_is = 'Owais is the best'
print(f"position is number {Owais_is.find('best')}")  # Returns the position (number) of 'best' in the string Owais_is
print("Owais" in Owais_is)  # Returns whether 'Owais' is inside the string Owais_is

print(50 * '_')

# displays whether statemet is true or not

Apples = random.randint(1, 100)
print(Apples < 10 or Apples > 50)
print(Apples)
