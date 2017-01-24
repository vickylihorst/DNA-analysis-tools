# author: Vicky Li Horst

workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
fileName = "pattern_match_test.txt"
#fileName = "vibrio-cholerae-genome.txt"


# This function takes the two strings, pattern and genome, and returns a collection of space-separted integers specifying all starting positions where pattern appears as a substring of genome.
def patternMatch(pattern,genome):
	k = len(pattern)
	positionList = []
	for i in range(0,len(genome)-k+1):
		if genome[i:i+k] == pattern:
			positionList.insert(i,i)
	position = " ".join(str(e) for e in positionList) # conver the list to a space-separated string
	return position

if __name__ == '__main__':
	with open(workingDir + fileName,"r") as file:
		pattern = file.readline().rstrip()
		genome = file.readline().rstrip()
		position = patternMatch(pattern,genome)
		print(position)




