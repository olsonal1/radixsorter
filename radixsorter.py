#=============================================
# A radix sorter for enumerable elements
# - by Alexander Olson.

#Radix sort is a handy and very simple algorithm to sort data that can be efficiently assigned an integer ordering of reasonable size.

#The algorithm has quite a few variations: you can read more about it in CLRS (or by its proper title, "Introduction to Algorithms" by
#Charles E. Leiserson, Clifford Stein, Ronald Rivest, and Thomas H. Cormen.

#Here, we implement it in python: we'll assume that we already have a list of elements, and- if they're not already integers-
#a function to cheaply enumerate them.

#If you'd like to use this for whatever (non-plagiarizing) reason, feel free! (But please attribute it).
#=============================================

#---------------------------------------------
#USAGE
#---------------------------------------------

#radixsort(A, f) will take two inputs:

# 1) A : the *list* of n inputs to be sorted.

# 2) f (optional) : a *function* that assigns a number to any given element of the list.
# If you don't provide and f, we'll use the identity function instead.

# Note that your function f will have time complexity f(n), and a range of outputs equal to n^g(n).
# If both f(n) and g(n) are O(1), radix sort will run in linear time!
# But it'll still do better than O(n lg(n)), if f(n), g(n) < lg(n).
# WARNING: If f can't turn an element of the list into an integer, you'll almost certainly run into errors!

#Once radixsort() is done, it'll return the elements sorted by the numbering given by f.

#---------------------------------------------
#QUICK COMPLEXITY ANALYSIS
#---------------------------------------------

#We pick some number s = ceil(lg(n)).
#We also measure the range of the outputs, and denote this m.

#The algorithm allocates an array "storage" of size (2^s) elements, for O(n) space in total (and thus only O(n) time):
#each element of the array is an empty list.

#We want to sort the list by each of its digits in log base (2^s), where we have lg(m)/s digits in total.
#Each pass over the array copies the entire list, puts it in the corresponding spot in "storage", and copies it out:
#this is done in space and time O(n). 
#Summing the time over each of the lg(m)/s passes, this process takes O(n lg(m)/lg(n)) time in total.

#In addition, we have to convert the entire array from elements to integers, in order to sort, and find the maximum and minimum result.
#This adds an extra O(n*f(n)) time.

#Our input m is bounded by n^g(n), for some function g(n):
#Our final time complexity is then 
#O((lg(m)/lg(n) + f(n)) * n), equal to
#O(g(n) + f(n))*n).

#Which is better than O(n lg(n)), if both g(n) and f(n) < lg(n).
#Ideally, g(n) and f(n) will be constant and this will run in linear time.

#---------------------------------------------
#CODE
#---------------------------------------------

import random
def radixsort(A, f=None):
	#If not given an f, use the identity instead.
	if f==None:
		def f(x): 
			return x

	#In a single pass, find the max and min, and tuple each element with its corresponding number.
	#This way we only calculate f(n) once for each element, if its more costly then we hope.
	#Call the resulting list B.
	min = 0
	max = 0
	n = len(A)
	B = []
	for i in range(0, n):
		d = f(A[i])
		C = (A[i], d)
		B.append(C)
		if d < min: 
			min = d
		if d > max: 
			max = d
		
	#Decrement each element's number by min. O(n) operations.
	for i in range(0, n):
		B[i] = (B[i][0], B[i][1] - min)

	m = max - min
	s = 0
	
	#Here, we calculate ceil(lg(n)).
	while (m > 0):
		s = s + 1
		m = m / 2
	
	#Now, we calculate the base we want to work with.
	sbase = pow(2, s)
	
	#Result is our final, sorted array of tuples: initialize this to B.
	result = B
	
	#We apply counting sorts on each digit base 2^s, starting with the smallest.
	divisor = 1
	while (divisor < max - min):
		#Sort each number into buckets, based on the current digit.
		D = []
		for i in range(0, sbase): 
			D.append([])
		for i in range(0, n): 
			D[(result[i][1] // divisor) % sbase].append(result[i])
			
		#Recreate result.
		result = []
		for i in range(0, sbase): 
			result.extend(D[i])
			
		#Move onto the next digit.
		divisor = divisor * sbase
		
	#Now that we're done, we untuple each element of "result" and return that.
	for i in range(0, n):
		result[i] = result[i][0]
		
	return result

#We'll test our sorter here.
import random
def main():
	#We pick min which is randomly distributed from 2^10, 2^11, ..., 2^15
	#We pick max which is a random number from (min*2) to (min*9).
	#Alternatively, you can define a different list A.
	A = []
	min = pow(2, random.randint(10, 16))
	max = min * random.randint(2, 10)
	for i in range(min):
		A.append(random.randint(min, max))
	
	#We pick f as the identity function (default), but you can choose something different.
	def f(x): 
		return x
	
	#Print the list, sort it, and print it again.
	print(A)
	B = radixsort(A, f)
	print(B)
	
	#We'll test if it was properly sorted (it should be!)
	#Compare each element with the next one, using our enumerating function f.
	for i in range(0, len(B) - 1):
		if f(B[i]) > f(B[i+1]):
			print("That didn't sort right.")
			return 0
	print("Looks sorted!")
	return 0

if __name__ == "__main__":
    main()