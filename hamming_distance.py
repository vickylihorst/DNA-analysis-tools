# Author: Vicky Li Horst
# This program finds the Hamming distance between two stirngs. The Hamming distance is the number of mismatches between two strings p and q, such that position i in k-mers p1...pk and q1...qk is a mismatch if pi doesn't equal to qi.

filename = "hamming_distance_test.txt"

# The function hammingDistance() takes two strings of equal lengh and outputs the Hamming distance between the strings.
def hammingDistance(s1, s2):
	if len(s1) != len(s2):
		return "lengths don't match"

	hammingDistance = 0 # Assume the hamming distance is 0
	for i in range(0, len(s1)):
		if s1[i] != s2[i]: #if there is a mismatch, add 1 to hammingDistance
			hammingDistance = hammingDistance + 1
	return hammingDistance



if __name__ == '__main__':
	with open("fixture/{0}".format(filename),"r") as file:
		string1 = file.readline().rstrip()
		string2 = file.readline().rstrip()
		hammingDistance = hammingDistance(string1,string2)
		print hammingDistance
