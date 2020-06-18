import re
#string = "ababbaabbb"
string = input("Enter string for regular expression (a+b)*abb : ").strip()

expression = re.compile( r'(a*b*)*abb')
resultObj = expression.search(string)
try:
	final = resultObj.group()
	p = True
except:
	p = False

if p and final == string :
	print("Matched: ",end='')
	print(final)
else:
	print("Not matching")
