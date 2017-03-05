# Author: Vicky Li Horst

#filename = "vibrio-cholerae-genome.txt"
filename = "pattern_count_test.txt"
# the structure of the input file is the first line is the genome, and the second line is the pattern


# this function returns the count of the occurance of a given pattern in the text by sliding the window one nucleotide at a time
def patternCount(text,pattern):
	count = 0
	for i in range (0,len(text) - len(pattern)+1):
		if text[i:i+len(pattern)] == pattern: # ensure the sliding window size is 1
			count = count + 1
	
	return count



	
if __name__ == "__main__":
	with open("fixture/{0}".format(filename),"r") as input:
		text = input.readline().rstrip() # use rstrip() to get rid of whitespace characters from the end of the string
		pattern = input.readline().rstrip()
		totalCount = patternCount(text,pattern)
		print(totalCount)
