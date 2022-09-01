
sauron = {"name" : "sauron", "no_rings" : 1, "ring_missing" : True, "address" : "mordor" , "popularity" : -1.025}

print(type(sauron))
print(sauron)

gandalf = {"name" : "Gandalf", "ring_missing" : False}
print(gandalf)

# Inserts new data into gandalf
gandalf["address"] = "none"
gandalf["no_rings"] = 1
gandalf["popularity"] = 98.27

print(gandalf)  # prints gandalf after new data inserted
print(gandalf["address"])  # prints gandalf's address
print(sauron["no_rings"])  # prints number of rings sauron has


# an if loop to locate if an element is in the dictionary and then printing its value
if "address" in sauron:
    print(sauron["address"])
else:
    print("sauron does not have a home")

# prints out all of the keys in the gandalf dictionary
for key in gandalf.keys():
    value = gandalf[key]
    print(f"{key} = {value}")
