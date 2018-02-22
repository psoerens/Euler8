###A class for reading in arrays of data into python


largeNumberTxt = '1000digit.txt'	#The file to be read from
i = 0	#line of the file
d = 0	#number of digits read in

largeNum = []	#instantiation of the new list representing the large number, set as integers
l = []			#temporary list

#rows, columns, number of digits in number
r = 0
c = 0
n = 0	


with open(largeNumberTxt) as file_object:	#open the object
	lines = file_object.readlines()			#read lines into a list
	
if (i == 0):	#comma separate variables of line "0"
	print(lines[i].rstrip())
	dims = lines[i].rstrip().split(",")
	r = int(dims[0])
	c = int(dims[1])
	n = int(dims[2])
	#print("rows: " + str(r) + ", cols:"+ str(c) + ", dig:" + str(n))
	i+=1	#index for the next line stored in lines

while d < n: #begin looping through the digit of the number
	l = lines[i].rstrip()
	#print(l)
	#print(len(l))
	strLen = len(l)
	
	if strLen > c:	#formatting error
		print('formatting error in file: line lenght longer than expected max lenth\n')
		SystemExit
	
	for digit in l:
		largeNum.append(int(digit))
	
	d+=strLen	#iterate through max length of line
	i+=1		#iterate to next line

print(i)
print(largeNum)