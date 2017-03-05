# author: Vicky Li Horst

filename = "pattern_match_test.txt"
#filename = "vibrio-cholerae-genome.txt"


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
	with open("fixture/{0}".format(filename),"r") as file:
		pattern = file.readline().rstrip()
		genome = file.readline().rstrip()
		position = patternMatch(pattern,genome)
		print(position)




