
# frequent_words

The function frequentWords() creates the algorithm for finding the most frequent k-mers in a DNA string.
The complexity of this algorith is O(n^2*k), where n is the length of the text.

The function fasterFrequentWords() performs the same job but increases performance.

The function patternToNumber() and patternToNumber2() solves the same problem, where they transform a k-mer pattern into an integer, which is the index of the pattern in the frequency array. The frequency array orders all 4^k k-mers lexicographically. The difference between the two functions is patternToNumber2() uses recursion.

# frequent_words_with_mismatch

Similar to frequent_words(), frequent_words_with_mismatch() finds the most frequent k-mer in a DNA string but with mismatches. The input is a string, and integers k and d (assumign k<=12 and d<=3). The output is most frequent k-mers with up to d mismatches in the string.


# pattern_count

This program counts the frequency of a given pattern in a genome. 


# reverse_complement_string

The function reverseComplementString() finds the reverse complement of a DNA string.


# pattern_match

The function patternMatch() takes the two strings, pattern and genome, and returns a collection of space-separted integers specifying all starting positions where pattern appears as a substring of genome.


# clump_finding

The function clumpFinding() outpus all distinct k-mers forming (L,t)-clumps in a genome, where L is the length of ori in the genome. A k-mer pattern forms an (L,t)-clump inside a genome if there is an interval of genome of length L in which this k-mer appears at least t times. The input is a string genome, and integers k, L, and t. A clump is also sometimes called a cluster.


# minimum_skew

The function minimumSkew() takes a DNA string and outputs all integer(s) i minimizing "Skew(genome) sub i" among all values of i for the entire input genome. The hypothesis is the integer(s) that minimizes the skew diagram is the origin of DNA replication. For more details on the hypothesis and the theory, see the comments in minimum_skew.py

The program can also plot the skew diagram by uncommenting the line `plt.show()`.


# hamming_distance

The function hammingDistace() finds the number of mismatches between two strings (aka the Hamming distance), such that position i in k-mers p1...pk and q1...qk is a mismatch if pi doesn't equal to qi, where p and q are two strings. 


# approximate_pattern_match

The function approximatePatternMatch() finds where a pattern appears as a substring of text with at most d mismatches. The function takes pattern, text, and an integer d, and outputs the total count and all starting positions where pattern appears as a substring of text with at most d mismatches.


# neighbors

The functino neighbors() generates the set of all k-mers whose Hamming distance from pattern doesn not exceed d.







