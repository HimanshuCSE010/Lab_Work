def decimal_to_gc():
	dec = int(input("Enter decimal number: "))
	offset = bin(dec)[3:]
	length = '1'*(len(offset)) + '0'
	print(f"{'Decimal':<10} {'Length':<20} {'Offset':<20} {'Gamma Code'}")
	print(f"{dec:<10} {length:<20} {offset:<20} {length+offset}")

def gc_to_decimal():
	gc = input("Enter Gamma Code: ")
	i = 0
	while gc[i] != '0':
		i += 1

	j = i+1
	res = ''
	while i > 0:
		res += gc[j]
		j += 1
		i -= 1
	binary = '1'+res
	
	print(f"{'Binary':<20} {'Decimal':<20}")
	print(f"{binary:<20} {int(binary,2)}")

def main():
    n = int(input("1. Deciaml to Gamma Code    2. gamma Code to Decimal: "))
    if n == 1:
        decimal_to_gc()
    else:
        gc_to_decimal()    

if __name__ == '__main__':
    main()
    
"""
Example Input
1
7

2
11011

2
1110100
"""