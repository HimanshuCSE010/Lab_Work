from collections import defaultdict
import sys
import os
# universal dictionary for dictinary and non positional posting
dictionary = defaultdict(list)

#sorted dictionary
posting_list = {}
# for relative access of documents
directory = __file__.split('/')
directory.pop()
seperator = os.sep
if os.name == 'nt':
        directory = seperator.join(directory) + 'Lib\\Documents\\'
else:
        directory = seperator.join(directory) + '/Documents/'

def ReadDoc(name,DocNo):
        path = directory+str(name)
        #print(path)
        # absolute path
        # path = 'E:\\Study\\Graduation\\Semester 6\\IR\\IR LAB\\Lib\\Documents\\' + name
        with open(path,'r') as doc:
                # reading documents
                s = doc.readline()
               
                # removing puncutation and delimiters
                s = s.replace(',','')
                s = s.replace('.','')
                s = s.lower()
                s = s.split()
                tokens = []
                stopwords = {'a', 'an', 'the', 'the', 'with', 'a', 'are', 'also', 'an', 'and', 'are', 'as', 'be', 'by', 'can', 'for', 'from', 'has', 'in', 'is', 'it', 'its', 'of', 'or', 'to', 'been', 'they', 'where'}

                #removing stopwords
                for i in s:
                        if i not in stopwords:
                                tokens.append(i)
                        
                #print(tokens)
                
                #removing pluralization case folding document wise
                tokens.sort()
                iterate = tokens[:]
                for token in iterate:
                        if token+'s' in tokens:
                                while token+'s' in tokens:
                                        tokens.remove(token+'s')                       
                        elif token+'es' in tokens:
                                while token+'es' in tokens:
                                        tokens.remove(token+'es')
                        elif token+'ies' in tokens:
                                while token+'ies' in tokens:
                                        tokens.remove(token+'ies')
                tokens = set(tokens)
                #print(tokens)
                for e in tokens:
                        if e in dictionary:
                                dictionary[e].append(DocNo)
                        else:
                                dictionary[e] = [DocNo]
        

def main():
        DocList = ['Doc1.txt', 'Doc2.txt', 'Doc3.txt', 'Doc4.txt']
        for i,d in enumerate(DocList):
                ReadDoc(d,i+1)  #document name, docID

        #sorted dictionary
        for e in sorted(dictionary.keys()):
	        posting_list[e] = dictionary[e]

        if os.name == 'nt':
                print_dict = lambda : print('{0:>13} -- {1:}'.format(ele,lst) ,end = '\t\t')
        else:
                print_dict = lambda : print('{0:>20} -- {1:<20}'.format(ele,lst) ,end = '\t\t')

        #print sorted dictionary
        ans = input("Show posting list(Y/N): ")
        if ans == 'Y' or ans == 'y':
                for ele,lst in posting_list.items():
                        lst = set(lst)
                        lst = ' '.join(map(str, lst))
                        print_dict()
                print("\n")

if __name__ == "__main__":
        main()
