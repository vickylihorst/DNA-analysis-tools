# Author: Vicky Li Horst
from frequent_words_with_mismatches import computingFrequenciesWithMismatches
from reverse_complement_string import reverseComplementString
from frequent_words import numberToPattern

filename = "frequent_words_with_mismatches_test.txt" # use the same file as frequentWordsWithMismatches()

# This functions finds the most frequent k-mers with mismatches and reverse complements in a DNA string.T
# The input is a DNA string Text, and integers k and d.
# The output is all k-mers maximazing the sum of Count(Text,Pattern) with d mismatches + Count(Text,Pattern-rc) with d mismatches over all possible k-mers
def frequentWordsWithMismatchesAndReverseComplements(text,k,d):

	frequentPatterns = set()
	forwardFrequencyArray = computingFrequenciesWithMismatches(text,k,d)
	#generate a reverseComplementFrequencyArray for the reverse complement string of the input DNA text
	reverseComplementFrequencyArray = computingFrequenciesWithMismatches(reverseComplementString(text),k,d)
	frequencyArray = [x + y for x,y in zip(forwardFrequencyArray,reverseComplementFrequencyArray)] # use zip() to aggregates the elements in the two arrays
	maxCount = max(frequencyArray)
	for i in range(0,4**k):
		if frequencyArray[i] == maxCount:
			pattern = numberToPattern(i,k)
			frequentPatterns.add(pattern)
	frequentPatternList = list(frequentPatterns) #convert a set to list
	return frequentPatternList



if __name__ == '__main__':
	with open("fixture/{0}".format(filename),'r') as file:
		text = file.readline().rstrip()
		secondLine=file.readline().rstrip().split()
		k = int(secondLine[0])
		d = int(secondLine[1])
		print(frequentWordsWithMismatchesAndReverseComplements(text,k,d))

