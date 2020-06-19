#Baysian Classification
"""
	Ex input
	1 1 1
	or
	0 0 0
"""

data = [
	[0,0,0],
	[0,0,1],
	[0,1,0],
	[0,1,1],
	[1,0,0]
]
		
target = [0,1,1,0,1]	

def Posterior_pro(Test,classification):
    num_attribute = len(data[0])
    result = [0]*num_attribute        
    num_samples = len(data)
    for j in range(num_samples):
        if target[j] == classification:
            if data[j][0] == Test[0]:
                result[0] += 1
            if data[j][1] == Test[1]:
                result[1] += 1
            if data[j][2] == Test[2]:
                result[2] += 1
    Class_count = target.count(classification)
    
    for i in range(num_attribute):
        result[i] = result[i]/Class_count
    return result

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p
                                
def main():
	print("*****    Baysian Classification    *****\n")
	num_samples = len(target)
	
	print("A1  A2  A3")
	for i in range(num_samples):
		print(data[i])
	
	# Test = list(map(int,input("Enter Test Case (A1 A2 A3): ").split()))
	Test = [1,1,1]
	print("Test Sample: ",Test)
	
	p_yes = target.count(1)/num_samples
	p_no = target.count(0)/num_samples
	
	print('')
	print('P(Yes) = ',p_yes)
	print('P(No) = ',p_no)

	posterior_yes = Posterior_pro(Test,1)   #yes
	posterior_no = Posterior_pro(Test,0)    #no
        
	print('')
	print('Posterior (X|Yes): ',posterior_yes)
	print('Posterior (X|No): ',posterior_no)        
        
	p_yes = p_yes * product(posterior_yes)
	p_no = p_no * product(posterior_no)
	
	print('')        
	print("P(Yes|X): ",p_yes)
	print("P(No|X): ",p_no)
	
	print('\n')
	if p_yes > p_no:
		print("***  X belong to class 1 (Yes Class) ***\n")
	elif p_yes < p_no:
		print("***  X belong to class 0 (No Class) ***\n")
	else:
		print("***  Cannot classify  ***\n")              

if __name__ == '__main__':
	main()
