# Author: Vikcy Li Horst
# This program aims to find the origin of DNA replication by following the peculiar statistics:
#  the difference between the guanine and cytosine counts changes from decreasing to increasing at the replication origion, when scanning through the genome in the 5' -> 3' direction
# Thus, we define the concept of "Skew(genome) sub i" to be the difference between the total number of occurrences of G and the total number of occurrences of C in the first i nucleotides of the genome.
# The skew should achieve a minimum at the position where the ori is.
# The peculiar statistics mentioned above make sense because of the nature of replication:
# DNA polymerase can only move in the 3'-> 5' direction of the parent strand, so one side of the strand will be copied continueously (we call it reverse half-strands as it's in the 3' -> 5' direction), while the other side will be copied dis-continueously (we call it forward half-strands), forming Okazaki fragments. The forward half-strands suffer delays, and spend much longer being single-stranded, compared to the reverse half-strands. Since single-stranded DNA has a much higher mutation rate than double-stranded DNA: if one of the four nucleotides in single-stranded DNA has a greater tendency than other nucleotides to mutate in single-stranded DNA, then we should observer a shortage of this nucleotide on the forward half-strand. Scientists discovered that cytosine has a tendency to mutate into thymine through a process called deamination, which rise 100-fold when DNA is single-stranded, resulting a decrease in cytosine on the forward half-strand. Also, since C-G base pairs eventually change into T-A base pairs, deamination results in decrease in guanine on the reverse half-strand. Thus there should be more guanine on the forward half-strand and more cytocine on the reverse half-strand, that is to say the difference between the total number of guanine and the total number of cytosine is positive on the forward half-strand, and negative on the reverse half-strand. With this knowledge, our goal is to traverse the genome, keeping a total count of the difference between the number of guanine and cytocine. If this difference starts increasing, then we are on the forward half-strand; if the difference starts decreasing, then we are on the reverse half-strand. When you read in the 5' -> 3' direction and notice the difference between G and C changed from decreasing to increasing, you are at the replication origin. Taking one step further, we can make a skew diagram by plotting "Skew(genome) sub i" as i ranges from 0 to then length of the genome, where "Skew(genome) sub 0" is zero. As we traversing the genome, we add 1 to the previous count if we encounter a G, subtract 1 to the previous count if we encounter a C, and keep the previous count if we encounter an A or T. This way, we are keeping a count of all nucleotides. When we find the lowest point(s) on that graph, we believe we find the ori.
import matplotlib.pyplot as plt

workingDir = "/Users/mli/Projects/DNA-analysis-tools/fixture/"
#fileName = "minimum_skew_sample.txt"
#fileName = "e_coli_clump_finding.txt" #This is the E.Coli dataset
fileName = "minimum_skew_test.txt"
# the function takes a DNA string and outputs all integer(s) i minimizing "Skew(genome) sub i" among all values of i for the entire input genome
def minimumSkew(genome):
	skew = []
	skew.append(0) # note the skew[0] = 0, so the lend of skew is the lengh of genome + 1
	for i in range(0,len(genome)):
		if genome[i].upper() == "C":
			skew.append(int(skew[i]) - 1)
		elif genome[i].upper() == "G":
			skew.append(int(skew[i]) + 1)
		elif (genome[i].upper() == "T") or (genome[i].upper() == "A"):
			skew.append(int(skew[i]))
	# To plot the skew diagram:	
	from math import log
	x = []
	for i in range(0,len(skew)):
		x.append(i)
	plt.plot(x,skew)
	plt.title("Skew Diagram")
	plt.xlabel("pisition")
	plt.ylabel("skew")
	# To show the skew diagram, uncomment the following line:
	plt.show()

	# create a minimal position list
	minPosList = []
	minVal = min(skew) # find the minimal value in the skew list
	for i in range(0,len(skew)):
		if skew[i] == minVal:
			minPosList.append(i) # add the position of the min value to the minPosList
	minPosString = " ".join(str(e) for e in minPosList) # turn the list into a string, separated by space
	return minPosString


if __name__ == '__main__':
	with open(workingDir + fileName,'r') as file:
		genome = file.readline().rstrip()
		minPosString = minimumSkew(genome)
		print(minPosString)
