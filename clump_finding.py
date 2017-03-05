# Author: Vicky Li Horst
from frequent_words import computingFrequencies
from frequent_words import patternToNumber
from frequent_words import numberToPattern
workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
filename = "clump_finding_test.txt"
#filename = "sample.txt" #this is the E. coli genome
# This function outpus all distinct k-mers forming (L,t)-clumps in genome, where L is the length of ori in the genome. The input is a string genome, and integers k, L, and t.
# The definition of a clump is a k-mer that appears many times within a short interval of the genome.
# a k-mer pattern forms an (L,t)-clump inside a genome if there is an interval of genome of length L in which this k-mer appears at least t times.
# Here we assume that the k-mer completely fits within the interval.
def clumpFinding(genome,k,t,L):
	frequentPatterns = set()
	clump = []
	for i in range(0,4**k): # initializing the list
		clump.append(0) 
	text = genome[0:L]
	frequencyArray = computingFrequencies(text,k) # compute the frequency array once here
	for i in range(0,4**k):
		if frequencyArray[i] >= t:
			clump[i] = 1 
	for i in range(1,len(genome)-L+1):
		# really the frequencyArray only changed the beginning and the end when sliding the window 1 nucleotide to the right
		firstPattern = genome[i-1:i-1+k] # the first k-mer in L
		index = patternToNumber(firstPattern)
		frequencyArray[index] = frequencyArray[index] - 1 # now we moved one nucleotide to the right, the new frequencyArray doesn't have the original first k-mer, so we minus one from the original array
		
		lastPattern = genome[i+L-k:i+L] # the end k-mer in L
		index = patternToNumber(lastPattern)
		frequencyArray[index] = frequencyArray[index] + 1 #now we moved one nucleotide to the right, we need to add the last k-mer in L to the original frequencyArray
		if frequencyArray[index] >= t:
			clump[index] = 1
	for i in range(0,4**k):
		if clump[i] == 1:
			pattern = numberToPattern(i,k)
			frequentPatterns.add(pattern)
	frequentPatternsList = list(frequentPatterns)
	frequentPatternsString = " ".join(str(e) for e in frequentPatternsList)
	return frequentPatternsString


if __name__=="__main__":
	with open ("fixture/{0}".format(filename),"r") as file:
		genome = file.readline().rstrip()
		secondLine = file.readline().rstrip()
		k = int(secondLine.split(' ')[0])
		L = int(secondLine.split(' ')[1])
		t = int(secondLine.split(' ')[2])
		frequentPatterns = clumpFinding(genome,k,t,L)
		print frequentPatterns



