#Author: Vicky Li Horst
from pattern_count import patternCount

workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
fileName = "frequent_words_test.txt"

# this function creates the algorithm for finding the most frequent k-mers in a DNA string by performing the following steps:
# 1. checking all k-mers in the DNA
# 2. computing how many times each k-mer appears in the DNA
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

	print(uniqueFrequentPatterns)
	return uniqueFrequentPatterns

if __name__ == "__main__":
	with open(workingDir+fileName, 'r') as input:
		text = input.readline().rstrip()
		k = 3		# looking for k-mer
		patterns = frequentWords(text,k)