""" PROGRAM THAT RETURNS A LIST OF BOOKS WRITTEN BY A USER INPUTTED AUTHOR"""

# Dictionary including a collection of Authors as the 'keys' and the book they have written as the 'values'
books = {"William Shakespeare": ["Hamlet", "Macbeth", "Romeo & Juliet"],
         "Stephen King": ["The Shining", "Rage", "Night Shift"],
         "JK Rowling": ["Harry potter and the sorcerer's stone", "Harry Potter and the chamber of secrets"],
         "JRR Tolkien": ["LOTR : The Return of the King", "LOTR : The Fellowship of the Ring", "The Hobbit"],
         "Roald Dahl" : ["Charlie and The Chocolate Factory" , "James and the Giant Peach" , "Matilda"],
         "Stan Lee" : ["Iron-Man" , "Spider-Man" , "Hulk"]}

Author_list = ", ".join(books)  # Turns the keys into a string allowing author names to be displayed as a list

print(f"Hello User! "
      f"\nThis program will provide you with a list of the most popular books written by a given author"
      f"|\n{50*'-'} "
      "\nPlease select an author from the following list:"
      f"\n{Author_list}")
print(50*'-')
author_name = input("*** PLEASE ENTER THE AUTHOR NAME EXACTLY AS SHOWN ABOVE *** "
                    "\n> ")


# loop which takes inputted author (keys) from user and locates this within the dictionary
# returning a list of the books (values)

if author_name in books:
    B = books[author_name].sort()  # sorts list of books (values) into alphabetical order before joined into a string
    A = ", ".join(books[author_name])
    print(f"{author_name} has written the following books: ")
    print(A)
else:
    print('You may have made a spelling mistake, please enter a valid author name!')

print(50*'-')
print("Thank you for using this automated Library service! ")
