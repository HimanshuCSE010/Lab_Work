import math 

def weightedkNN(points,p,k=3): 
	distance=[] 
	for group in points: 
		for feature in points[group]: 
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 
			distance.append((euclidean_distance,group)) 

	distance = sorted(distance)[:k] 
	freq1 = 0 # weighted sum of group 0 
	freq2 = 0 # weighted sum of group 1 

	for d in distance: 
		if d[1] == 0: 
			freq1 += (1 / d[0]) 
			
		elif d[1] == 1: 
			freq2 += (1 /d[0]) 
			

	return 0 if freq1>freq2 else 1

def main(): 
	# data
	points = {0:[(0, 4),(1, 4.9),(1.6, 5.4),(2.2, 6),(2.8, 7),(3.2, 8),(3.4, 9)], 
			1:[(1.8, 1),(2.2, 3),(3, 4),(4, 4.5),(5, 5),(6, 5.5)]} 
	# query point 
	p = (2, 4) 
	# Number of neighbours 
	k = 5
	print("\nClasses: 0 and 1")
	print("Query point is: ",p)
	print("Choosen value of K: ",k)
	print("The Class assigned after classification is: {}".format(weightedkNN(points,p,k))) 

if __name__ == '__main__': 
	main() 
