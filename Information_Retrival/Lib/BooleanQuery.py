from . import NonPositionalPosting as npp

def main():
	npp.main()		#now we have inverted index as 'posting_list'

	query = input("Write a boolean query: ")
	q_or = query.split('OR')		#splitting from OR keywords
	result = set()					#final set to contain results
	for i in q_or:					
		temp = set()
		q_and = i.split('AND')		#splitting each OR phrase from AND
		q_and = [x.strip() for x in q_and]	#removing side space from each word

		lst = npp.posting_list[ q_and[0] ]	#gettting list of first word
		temp.update( set(lst) )				#adding element by element
		for t in range(1,len(q_and)-1):		#intersection
			temp = temp.intersection(set( npp.posting_list[ q_and[t] ] ))	
		result = result.union(temp)			#union of temp to final result

	print('Required Document ID: ',*result)

if __name__ == "__main__":
	main()
# vines AND plant OR trees AND most OR widely
# 1 2 4