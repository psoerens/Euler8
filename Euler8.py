twenty = [1,2,3,4,5,6,7,8,9,0,1,3,5,7,9,2,4,6,8,0] #testing list

index = 0	#initial index
lens = 4 #length of lens

length = len(twenty)
last = length - lens+1 #last index to check
#print(last)
largeMulti = 0 #The largest product so far

for i in range(index, last) :
	
	temp = (twenty[i])*(twenty[i+1])*(twenty[i+2])*(twenty[i+3])
	print(temp)
	
	if temp > largeMulti:
		largeMulti = temp
	
print(i)
print(largeMulti)