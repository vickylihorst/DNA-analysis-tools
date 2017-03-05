# Author: Vicky Li Horst
from hamming_distance import hammingDistance
workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
filename = "frequent_words_with_mismatches_test.txt"
# The function frequentWordsWithMismatches() finds the most frequent k-mers with mismatches in a string
# The input is a string, and integers k and d (assumign k<=12 and d<=3). The output is most frequent k-mers with up to d mismatches in the string.
def frequentWordsWithMismatches(text, k, d):
	frequentPatterns = set()
	neighborhoods = []
	#for i in range(0,len(text)-k+1):



	return
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
	neighborhoodList = neighbors("CAACGCAC",2)
	print("\n".join(neighborhoodList))
	#print(neighbors("ACG",1))
	# with open(workingDir+filename,"r") as file:
	# 	text = file.readline().rstrip()
	# 	secondLineList = file.readline().rstrip().split()
	# 	k = secondLineList[0]
	# 	d = secondLineList[1]
	# 	frequentWordsWithMismatches(text,k,d)
		