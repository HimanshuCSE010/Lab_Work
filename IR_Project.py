import os
import sys
import Lib.edit as ed
import Lib.NonPositionalPosting as npp
import Lib.BooleanQuery as bq
import Lib.wildcard as wc
import Lib.VariableByteCode as vbc
import Lib.GammaCode as gc
import Lib.Rocchio as Rocchio
import Lib.KNN as KNN
import Lib.NaiveBayes as NB
import Lib.Kmeans as Kmeans
import Lib.TopKdoc as topK
#To clear the console screen
if os.name == 'nt':
        clear = lambda: os.system('cls')
else:
        clear = lambda: os.system('clear')

def main():
	clear()
	print("***********************************IR System***********************************")
	print("1. Calculate Edit Distance")
	print("2. Show Inverted Index of all documents")
	print("3. Make Boolean query")
	print("4. Make wild card query")
	print("5. Convert DocID to Variable Byte Code or reverse")
	print("6. Decimal to Gamma Code and reverse")
	print("7. Rocchio Classification")
	print("8. KNN Classification")
	print("9. Naive Bayesian Classification")
	print("10. Flat Clustering -> k-Means")
	print("11. Retrive Rankwise all documents for a query")
	n = int(input("Enter Choice (0 to quit) : "))

	if n == 1:	#Edit distance
		ed.main()
	elif n == 2:
		npp.main()
	elif n == 3:
		bq.main()
	elif n == 4:
		wc.main()
	elif n == 5:
		vbc.main()
	elif n == 6:
		gc.main()
	elif n == 7:
		Rocchio.main()
	elif n == 8:
		KNN.main()
	elif n == 9:
		NB.main()
	elif n == 10:
		Kmeans.main()
	elif n == 11:
		topK.main()
	else:
		print("Exiting.....")

if __name__ == "__main__":
	while True:
		main()
		# to flush input buffer so that input() actually stop for input
		# sys.stdout.flush()	# is also an alternate
		sys.stdin.flush()
		i = input("To exit press Q: ")
		if i == 'q' or i == 'Q':
			print("Exiting......")
			break
