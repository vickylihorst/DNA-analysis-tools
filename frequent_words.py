#Author: Vicky Li Horst
from pattern_count import patternCount
from collections import deque

workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
fileName = "frequent_words_test.txt"
#fileName = "pattern_to_number_test.txt"
# The format of the file is: DNA in the first line, and the k-mer integer in the second line.

# This function creates the algorithm for finding the most frequent k-mers in a DNA string by performing the following steps:
# 1. checking all k-mers in the DNA
# 2. computing how many times each k-mer appears in the DNA
# Note: the complexity of this algorithm is O(n^2*k), where n is the length of the text.

def frequentWords(text, k):
	frequentPatterns = []
	countList = []
	for i in range(0,len(text)-k+1):
		pattern = text[i:i+k]
		countList.insert(i,patternCount(text,pattern))
	maxCount = max(countList)
	
	for i in range(0, len(text)-k+1):
		if countList[i] == maxCount:
			frequentPatterns.insert(i,text[i:i+k])
	# use a set to remove duplicates from frequentPatterns, since sets are unordered collections of distinct objects
	uniqueFrequentPatterns = list(set(frequentPatterns))
	return uniqueFrequentPatterns

#==================To improve performance=================

# This funciton transforms a k-mer pattern into an integer, which is the index of the pattern in the frequency array.
# The frequency array orders all 4^k k-mers lexicographically.
# For example, the pattern ATGCAA corresponds to the integer 912, because 0*4^0+0*4^1+1*4^2+2*4^3+3*4^4+0*4^5 = 912, where A=0, C=1, G=2, T=3. 
def patternToNumber(pattern):
	base4result = []
	result = 0
	# take the pattern and converts it to a base-4 integer, following the mapping where A=0, C=1, G=2, T=3.
	for e in pattern:
		if e.upper() == "A":
			base4result.append(0)
		elif e.upper() == "C":
			base4result.append(1)
		elif e.upper() == "G":
			base4result.append(2)
		elif e.upper() == "T":
			base4result.append(3)

	# convert the base-4 integer to a base-10 integer.
	for j in range(0,len(base4result)): 
		result = result + base4result[len(base4result) - j - 1] * 4**j
	return result


	
# This function is the reverse of PatternToNumber(), where it transforms an integer between 0 and 4^k-1 into a k-mer.
# For example, the output of numberToPattern(5437,7) is CCCATTC, because the raminder of 5437/4 for each step in reverse order is 1110331, where A=0, C=1, G=2, T=3.
# Another example, the output of numberToPattern(5437,8) is ACCCATTC, because you devide the last number 0 by 4 again to get the eighth digit.
def numberToPattern(index,k):
	# convert the index number to a base-4 integer.
	remainderList = deque() # use a double-ended queue, so I can do appendleft() instead of append() and reverse()
	integer = index
	pattern = []
	for i in range(0,k):
		remainder = integer % 4
		integer = integer // 4
		remainderList.appendleft(remainder)
	#now take the remainderList, and outputs the corresponding DNA sequence following the mapping where A=0, C=1, G=2, T=3
	for e in remainderList:
		if e == 0:
			pattern.append("A")
		elif e == 1:
			pattern.append("C")
		elif e == 2:
			pattern.append("G")
		elif e== 3:
			pattern.append("T")	
	patternString = "".join(str(e) for e in pattern) #list to string
	return patternString

# The algorithm makes a single pass through the text. For each k-mer, add 1 to the value of the frequency array corresponding to the pattern. 
# The frequency array orders the k-mers lexicographically.
def computingFrequencies(text,k):
	frequencyArray = [] # note: the datatype is a list here. It's called a frequencyArray for conceptual reasons
	# we need to first initialize the frequencyArray because later on we add 1 to the corresponding position
	for x in range(0,4**k): 
		frequencyArray.append(0)
	for i in range(0,len(text)-k+1):
		pattern = text[i:i+k]
		j = patternToNumber(pattern)
		frequencyArray[j] = frequencyArray[j] + 1
	return frequencyArray

# This function produces the same result as frequentWords(), but with better performance. The complexity of the algorithm is O(n*k) where n is the length of the text.
def fasterFrequentWords(text,k):
	frequentPatterns = set()
	frequencyArray = computingFrequencies(text,k)
	maxCount = max(frequencyArray)
	for i in range(0,4**k):
		if frequencyArray[i] == maxCount:
			pattern = numberToPattern(i,k)
			frequentPatterns.add(pattern)

	frequentPatternList = list(frequentPatterns) #convert a set to list
	return frequentPatternList


if __name__ == "__main__":
	with open(workingDir+fileName, 'r') as input:
		text = input.readline().rstrip()
		k = int(input.readline().rstrip())
		#patterns = frequentWords(text,k)
		#print(patterns)
		#patternToNumber(text)
		#frequencyArray = computingFrequencies(text,k)
		#print(frequencyArray)
		#convert the frequentArray list to a string concatenated by space
		#frequencyArrayString = " ".join(str(x) for x in frequencyArray) # need to convert each element in the list before joining them
		#print(frequencyArrayString)
		#pattern = numberToPattern(6,3)
		#print(pattern)
		#print(nucleotideToNumber("ATCG"))
		frequentPatterns = fasterFrequentWords(text,k)
		print(frequentPatterns)




