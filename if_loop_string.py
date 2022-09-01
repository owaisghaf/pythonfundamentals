text = "help world"
print(text.count("o"))

if text.startswith("hell"):  # if this condition is true do this
    print("it's hell in there!")
elif text.startswith("help"):  # else if this condition is true do this
    print("please help me")
else:
    print("it's heaven in there!")

if text.isalpha():
    print("string is all alpha")
else:
    print("string is not alpha")

text = "\t\r\n"  # nothing in text because \ tells python to ignore the letters
if text.isspace():
    print("string is whitespace")
else:
    print("string is not whitespace")
