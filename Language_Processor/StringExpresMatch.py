import re
exp = input("Enter Regular expression using only (* . ^ $ * + ?) as per python docs : ").strip()
string = input("Enter String to be verified: ").strip()

regexpresion = re.fullmatch(exp,string)
if regexpresion:
    print("\nMatched")
else:
    print("\nNot Matched")

