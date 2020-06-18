# import NonPositionalPosting as npp 
from . import NonPositionalPosting as npp 
import re

def main():
    npp.main()
    result = []
    i = int(input("Use 1. regular expression  2. python expression: "))
    if i == 1:
        pattern = input("Enter regular expression allowed symbols (*): ")
        a = pattern.index('*')
        pattern = pattern[:a] + '.*' + pattern[a+1:]
    else:
        pattern = input("Enter regular expression allowed symbols (as per re module): ")
    for k,v in npp.posting_list.items():
        if re.fullmatch(pattern, k):
            result.append( [k,v] )
    for i in range( len(result) ):
        ele = result[i][0]
        lst = ' '.join(map(str, set(result[i][1]) ))
        print( '{0:>15} -- {1:<15}'.format(ele,lst) )

if __name__ == '__main__':
    main()
    