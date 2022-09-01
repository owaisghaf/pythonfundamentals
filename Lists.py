""" LISTS """

owais_list = ["a", "b", "c", "d", "e", "b"]

owais_list.insert(0, "this is first")  # inserts 'this is first' in position 0 moving everything to the right
print(owais_list)

owais_list.pop(5)  # removes 5th value from list
print(owais_list)

owais_list.remove("b")  # removes first instance of 'b' in list
print(owais_list)

del owais_list[1]  # deletes 3rd item in list
print(owais_list)

is_there = "c" in owais_list
print(is_there)

print(50*'_')

""" Lists within lists """

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]  # creates lists within a list
print(cool_animals)
print(cool_animals[-1][-1])  # prints the last element in the last list.

print(50*'_')

""" TUPLES """

# faster than strings or integers
# tuples cannot be altered unlike strings or lists

perfect_squares = (1, 4, 9, 16, 25, 36)

print(type(perfect_squares))

print(50*'_')

perfect_squares = (1, 4, 9, 16, 25, 36, 1, 4, 1, 2, 4)
print(type(perfect_squares))
farm = "Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850  # This is a tuple of length 3
farm_name, cool_cows, farm_size = farm
print(farm_name)
print(perfect_squares.count(4))
print(perfect_squares.index(36))

print(50*'_')

""" SETS """

test = {42, True, 'Bilbo', 'Frodo', 'Bilbo'}  # set. Values are not set in positions.
print(test)
print(len(test))