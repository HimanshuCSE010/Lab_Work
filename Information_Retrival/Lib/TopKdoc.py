from collections import OrderedDict
from math import sqrt

def main():
    voc_term = int(input("Enter number of terms in vocabulary: "))
    vocabulary = OrderedDict()
    for i in range(voc_term):
        print(f"Term and idf {i+1}: ",end='')
        term,idf = input().split()
        vocabulary[term.lower()] = float(idf)

    doc_no = int(input("Enter number of documents: "))
    docs = []
    for i in range(doc_no):
        print(f"Enter term frequency for doc{i+1}")
        doc = OrderedDict()
        sq = 0

        # getting term frequency of each term in each document
        for t,v in vocabulary.items():
            doc[t] = int(input(f"{t}: "))*v
            sq += doc[t]**2
        sq = sqrt(sq)
        
        # normalize
        for t,v in doc.items():
            doc[t] = round(v/sq, 3)

        docs.append([i,doc])
        print()
    
    print("Normalized Document Vectors")
    for i in range(doc_no):
        print(f"DocNo{i+1}:")
        for t,v in docs[i][1].items():
            print(f"{t:<10} {v:<5}",end=' | ')
        print()

    # getting test doc ready
    test_doc = OrderedDict()
    query = input("Enter query: ").lower().split()
    for t in vocabulary.keys():
        if t in query:
            test_doc[t] = 1
        else:
            test_doc[t] = 0
    
    score = []
    for d in range(doc_no):
        s = 0
        for t,v in docs[d][1].items():
            s += test_doc[t]*v
        score.append([s,'D'+str(d+1)])

    # getting result
    score.sort(key = lambda x: x[0], reverse = True)
    print("\nScores: ",*score)
    result = [ doc[1] for doc in score ]
    print("\nDocument Ranking for Query: ",*result)


if __name__ == '__main__':
    main()


"""
4
Car 1.65
Auto 2.08
Insurance 1.62
Best 1.5
3
27
3
0
14
4
33
33
0
24
0
29
17
car insurance
"""