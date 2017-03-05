# Author: Vicky Li Horst
# The observation is that a DnaA box may appear with slight variations. Thus, the goal is to find where a pattern appears as a substring of text with at most d mismatches.

from hamming_distance import hammingDistance

filename = "approximate_pattern_match_test.txt"
#fileName = "approximate_pattern_match_sample.txt"

# The function approximatePatternMatch() takes pattern, text, and an integer d, and outputs the total count and all starting positions where pattern appears as a substring of text with at most d mismatches
def approximatePatternMatch(pattern,text,d):
	startingPosList = []
	for i in range(0,len(text)-len(pattern)+1):
		if hammingDistance(pattern,text[i:i+len(pattern)]) <= d:
			startingPosList.append(i)
	count = len(startingPosList) # the length of the startingPosList is the number of times the pattern matches the string with at most d mismatch
	#print(count) 
	#convert the startingPosList to a string with space as the delimiter
	startingPos = " ".join(str(e) for e in startingPosList)
	return count,startingPos

if __name__ == '__main__':
	with open("fixture/{0}".format(filename),"r") as file:	
		pattern = file.readline().rstrip()
		text = file.readline().rstrip()
		d = int(file.readline().rstrip())
		count,startingPos = approximatePatternMatch(pattern,text,d)
		print(count)
		print(startingPos)