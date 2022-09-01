""" For loops for iterations """

# For loop is a lot more compact and requires less code to achieve the same thing

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5]

for item in numbers1:
    print(item)

print(50*'_')

# if loop which does the same as the for loop above but longer.

i = 0
while i < len(numbers2):
    print(numbers2[i])
    i = i + 1

print(50*'_')

# Does the same as the above loops but prints out each letter in the string

name_list = 'Owais'

for num in name_list:
    print(num)


# creates a range from 0 to 8 (the length of numbers 3).
# inputs i = 0 into the if loop and takes numbers3[0] and compares to 5. as it is smaller it will not print
# i is increase by 1 and iterated back in with numbers3[1] which is 5 being put into the if.
# This cycles through until all values up to length(numbers3) and values in the list have been cycled.

numbers3 = [1, 5, 7, 4, 6, 12, 46, 34]

for i in range(0, len(numbers3)):
    if numbers3[i] > 5:
        print(numbers3[i])
        i = i + 1
