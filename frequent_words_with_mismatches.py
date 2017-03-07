# Author: Vicky Li Horst
from hamming_distance import hammingDistance
from frequent_words import patternToNumber
from frequent_words import numberToPattern

filename = "frequent_words_with_mismatches_test.txt"

# The function frequentWordsWithMismatches() finds the most frequent k-mers with mismatches in a string
# The input is a string, and integers k and d (assumign k<=12 and d<=3). The output is most frequent k-mers with up to d mismatches in the string.
# The algorithm makes a single pass through the text. For each k-mer with up to d mismatches, add 1 to the value of the frequency array corresponding to the pattern. 
# The frequency array orders the k-mers lexicographically.
def frequentWordsWithMismatches(text,k,d):
	frequentPatterns = set()
	frequencyArray = computingFrequenciesWithMismatches(text,k,d)
	maxCount = max(frequencyArray)
	for i in range(0,4**k):
		if frequencyArray[i] == maxCount:
			pattern = numberToPattern(i,k)
			frequentPatterns.add(pattern)

	frequentPatternList = list(frequentPatterns) #convert a set to list
	return frequentPatternList



# The function computingFrequenciesWithMismatches() computes the frequency array with up to d mismatches
# The algorithm goes through the text, and for each k-mer with up to d mismatches, adds 1 to the frequency array corresponding to the pattern. The frequency array orders the k-mers lexicographically.
def computingFrequenciesWithMismatches(text,k,d):
	frequencyArray = [] # note: the datatype is a list here. It's called a frequencyArray for conceptual reasons
	# we need to first initialize the frequencyArray because later on we add 1 to the corresponding position
	for x in range(0,4**k): 
		frequencyArray.append(0)
	for i in range(0,len(text)-k+1):
		pattern = text[i:i+k]
		neighborhood = neighbors(pattern,d) # neighborhood is of a list
		for approximatePattern in neighborhood:
			j = patternToNumber(approximatePattern)
			frequencyArray[j] = frequencyArray[j] + 1
	return frequencyArray

# The function neighbors() generates the set of all k-mers whose Hamming distance from pattern doesn not exceed d.
# The input is a string pattern and an integer d, and the output is the collection of strings (one per line).
def neighbors(pattern,d):
	if d == 0: # if Hamming distance is 0, then return the pattern itself in a list format
		return pattern.split()
	if len(pattern) == 1: 
		return ['A','T','C','G'] # if the length of the pattern is 1 (and d doesn't equal to 0), then return ['A','T','C','G']
	neighborhood = set()
	suffixNeighbors = neighbors(pattern[1:],d) # suffixNeighbors is passing the last k-1 mer and d to the neighbors()
	for text in suffixNeighbors: #for each element in suffixNeighbors
		if hammingDistance(pattern[1:],text) < d:
			for e in ['A','T','C','G']:
				neighborhood.add(e+text)  
		else:
			neighborhood.add(pattern[0]+text)

	neighborhoodList = list(neighborhood)
	return neighborhoodList

if __name__ == '__main__':
	#neighborhoodList = neighbors("CAACGCAC",2)
	#print("\n".join(neighborhoodList))
	#print(computingFrequenciesWithMismatches("ACG",2,1))
	#print(neighbors("ACG",1))
	with open("fixture/{0}".format(filename),"r") as file:
		text = file.readline().rstrip()
		secondLineList = file.readline().rstrip().split()
		k = int(secondLineList[0])
		d = int(secondLineList[1])
		#print(computingFrequenciesWithMismatches(text,k,d))
		print(frequentWordsWithMismatches(text,k,d))
		