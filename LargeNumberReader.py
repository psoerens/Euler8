class LargeNumberReader():
	'''A class for reading in large numbers into python'''

	def __init__(self, file):
		'''Initialization via pasing in the text file to be read'''
		self.largeNumberTxt = file	#set the textfile attribute
		
	def getLarge(self):
		'''get the large number, parse through the file'''
		'''The expected format is:
			line 0: rows, columns, number of digits
			line [1:r]: the digits on lines not longer than columns
		'''
		
		#largeNumberTxt = '1000digit.txt'	#The file to be read from
	
		with open(self.largeNumberTxt) as file_object:	#open the object
			lines = file_object.readlines()			#read lines into a list
			
		i = 0	#line of the file
		d = 0	#number of digits read in
		largeNum = []	#instantiation of the new list representing the large number, set as integers
		
		if  i == 0:	#comma separate variables of line "0"

			#print(lines[i].rstrip())
			dims = lines[i].rstrip().split(",")
			r = int(dims[0])
			c = int(dims[1])
			n = int(dims[2])
			print("rows: " + str(r) + ", cols:"+ str(c) + ", dig:" + str(n))
			i+=1	#index for the next line stored in lines

		
		while d < n: #begin looping through the digit of the number
			l = lines[i].rstrip()
			#print("this is l " + l)
			#print("this is its length " + str(len(l)))
			#print("this is number of digits total " + str(n))
			strLen = len(l)
			
			if strLen > c:	#formatting error
				print('formatting error in file: line lenght longer than expected max lenth\n')
				SystemExit
			
			for digit in l:
				largeNum.append(int(digit))
			
			d+=strLen	#iterate through max length of line
			i+=1		#iterate to next line
			
		return largeNum



