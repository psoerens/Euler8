from LargeNumberReader import LargeNumberReader #useing the large number reader


lnr = LargeNumberReader('1000digit.txt')	#initialize the reader
large = lnr.getLarge()						#get the large number in a list format


index = 0	#initial index
lens = 13 #length of lens

length = len(large)	#length of the list
last = length - lens+1 #one beyond the last index to check
#print("The ending index to exit: " + str(last))

largeMulti = 0 #The largest product so far
indexFound = [0] * lens #range where found
#print(indexFound)
for i in range(index, last) :
	
	temp = large[i]	#store the fist value
	for j in range(1,lens) :
		temp *= large[i+j] #get product with remaining values in lens range
	#print(temp)
	
	if temp > largeMulti:
		largeMulti = temp
		
		for j in range(0, lens):	#largest product indexes
			indexFound[j] = i + j
			
	
#print("index gotten to at exit: " + str(i))
print("larges value found: " + str(largeMulti))
#print("found at: " + str(indexFound))