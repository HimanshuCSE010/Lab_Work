def bin_to_VB(b):
    if len(b)%7 != 0:
        res = -len(b)%7
        b = '0'*res + b
    
    code = []
    code.append( '1' + b[-7:] )
    b = b[:-7]
    while len(b) > 0:
        code.append( '0'+b[-7:] )
        b = b[:-7]
    return ','.join(code[::-1])
    

def Doc_to_VB():
    DocID = sorted(list(map(int, input("Enter docID's: ").split())))
    n = len(DocID)
    for i in range(n-1,0,-1):
        DocID[i] = DocID[i] - DocID[i-1]
    print("\nGap Sequence: ",*DocID)

    print(f"{'Gap Sequence':<15} {'Binary':<30} {'Varible Byte Code'}")
    for docID in DocID:
        binary = bin(docID)[2:]
        print(f"{docID:<15} {binary:<30} {bin_to_VB(binary)}")

def VB_to_Doc():
    Code_VB = input("Enter VB Code (',' or 'space' seperated): \n")
    if ',' in Code_VB:
        Code_VB = Code_VB.split(',')
    else:
        Code_VB = Code_VB.split()
    
    binary = []
    for vb in Code_VB:
        binary.append( vb[1:] )
    binary = ''.join(binary)
    binary = binary.lstrip('0')
    print(f"{'Binary':<30} {'Integer Value'}")
    print(f"{binary:<30} {int(binary,2)}")


def main():
    n = int(input("1. DocID to Variable Byte Code    2. Variable Byte Code to DocID: "))
    if n == 1:
        Doc_to_VB()
    else:
        VB_to_Doc()    

if __name__ == '__main__':
    main()
    
"""
Example Input
1
800 900 1245 5000 76453 932456

2
00110100,00011111,11000011
"""