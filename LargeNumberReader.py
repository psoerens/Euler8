###A class for reading in arrays of data into python


from array import array

#declaration	
a = array('i')	

largeNumberTxt = '1000digit.txt'	#The file to be read from
i = 0	#line of the file
d = 0	#number of digits read in

#rows, columns, number of digits in number
r = 0
c = 0
n = 0	
	
with open(largeNumberTxt) as file_object:	#open the object
	lines = file_object.readlines()			#read lines into a list
	
if (i == 0):	#comma separate variables of line "0"
	#print(lines[i].rstrip())
	dims = lines[i].rstrip().split(",")
	r = int(dims[0])
	c = int(dims[1])
	n = int(dims[2])
	#print("rows: " + str(r) + ", cols:"+ str(c) + ", dig:" + str(n))
	i= i+1	#index for the next line stored in lines

while d < n: #begin looping through the 
	while 
	


# :
	# for line in lines:
		# i=i+1
		# print(file_object.read())
