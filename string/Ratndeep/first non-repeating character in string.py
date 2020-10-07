N = 256
def NonRepeating(): 
	inDLL = [] * N
	repeated = [False] * N
	n = int(input())
	stream = input().split()
	for i in range(n): 
		x = stream[i] 
		if not repeated[ord(x)]: 
			if not x in inDLL: 
				inDLL.append(x) 
			else: 
				inDLL.remove(x) 
				repeated[ord(x)] = True
		if len(inDLL) != 0: 
			print (str(inDLL[0]),end=" ") 


for i in range(int(input())):
    NonRepeating() 
    print()
