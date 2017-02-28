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
# The input is a string pattern and an integer d, and the output is the collection of strings (one per line)
def neighbors(pattern,d):
	if d == 0:
		return pattern.split()
	if len(pattern) == 1:
		return ['A','T','C','G']
	neighborhood = set()
	suffixNeighbors = neighbors(pattern[1:],d) # suffixNeighbors is passing (the last k-1 mer,d) to the neighbors()
	for text in suffixNeighbors: #for each element in suffixNeighbors
		if hammingDistance(pattern[1:],text) < d:
			for e in ['A','T','C','G']:
				neighborhood.add(e+text) # replacing the 
		else:
			neighborhood.add(pattern[0]+text)

	# for i in range(0,len(pattern)):
	# 	symbol = pattern[i]
	# 	for e in ['A','T','C','G']:
	# 		neighbor = pattern[0:i]+e+pattern[i+1:]
	# 		neighborhood.add(neighbor)
	neighborhoodList = list(neighborhood)
	return neighborhoodList
	#print type(neighborhoodList)
	#return "\n".join(['ACC', 'ATG', 'AAG', 'ACG', 'GCG', 'AGG', 'ACA', 'ACT', 'TCG', 'CCG'])
	#return "\n".join(neighborhoodList)

if __name__ == '__main__':
	neighborhoodList = neighbors("ACG",1)
	print("\n".join(neighborhoodList))
	#print(neighbors("ACG",1))
	# with open(workingDir+filename,"r") as file:
	# 	text = file.readline().rstrip()
	# 	secondLineList = file.readline().rstrip().split()
	# 	k = secondLineList[0]
	# 	d = secondLineList[1]
	# 	frequentWordsWithMismatches(text,k,d)
		