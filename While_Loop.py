""" While loop iteration """

# iterates loop until you have inputted the names of 5 people
#
names = 0
print(f"type the names of 5 people one at a time")

while names < 5:
    print(f"type the name of person {names +1}")
    person = input()  # Does not have an impact on the value of names. Pauses code and won't proceed without input
    print(f"{person} is awesome!")
    names = names + 1  # adds 1 to value of names each time. loop will stop when names is => 5.

