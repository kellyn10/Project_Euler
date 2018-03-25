''' If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
Find the sum of all the multiples of 3 or 5 below 1000. '''

def euler1():
	n = 1000
	lst3 = [] ##List of multiples of 3 and 5 -- will avoid double counting

	for k in range(1,n):
		if (k % 3 == 0) or (k % 5 == 0):
			lst3.append(k)
	#return lst3  # -- for some reason, this will print the list but not the sum		
	sumlst = sum(lst3)
	return sumlst
	print (sumlst) 
euler1()


''' An attempt to generalize to all n, and store the list '''

# LIST OF MULTIPLES OF 3 AND 5 BELOW n

# def mlst(n): ### list of multiples of 3 and 5
	# lst = []
	# for k in range(1,n):
		# if (k % 3 == 0) or (k % 5 == 0):
			# lst.append(k)
	# return lst	
# mlst(n)

# #### ------------------------------------ #####

# # SUM OF A LIST

# def euler1_1(lst):
	# return sum(lst)
# euler1_1(lst)
# print ( euler1_1(mlst(1000)) )


