#Author: Vicky Li Horst

from collections import deque

filename = "reverse_complement_string_test.txt"

# This function finds the reverse complement of a DNA string.
# For example, if the input is AAAACCCGGT, then its reverse complement string is ACCGGGTTTT.
def reverseComplementString(text):
	reverseDeque = deque() # use a double-ended queue, so I can do appendleft() instead of append() and reverse()
	for n in text:
		if n.upper() == "A":
			reverseDeque.appendleft("T")
		elif n.upper() == "T":
			reverseDeque.appendleft("A")
		elif n.upper() == "C":
			reverseDeque.appendleft("G")
		elif n.upper() == "G":
			reverseDeque.appendleft("C")
	#convert the deque to a list
	reverseList = list(reverseDeque)
	#conver the list to a string
	reverseString = "".join(str(e) for e in reverseList)
	return reverseString

if __name__ == '__main__':
	with open("fixture/{0}".format(filename),"r") as input:
		text = input.readline().rstrip() # the format of the input file is one line of a DNA string
		reverse = reverseComplementString(text)
		# could write the result to a file if the input string is long
		print reverse