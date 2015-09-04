from dna_seq_hw1 import readGenome, readFastq

def editDistanceOfBM(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
       
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0
       
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
       
    # Edit distance is the value in the bottom right corner of the matrix
    return min(D[len(x)])


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


genome = readGenome('chr1.GRCh38.excerpt.fasta')

#Q1
#print editDistanceOfBM('GCTGATCGATCGTACG',genome)

#Q2
#print editDistanceOfBM('GATTTACCAGATTGAG',genome)

#Q3

seqs, quals = readFastq('ERR266411_1.for_asm.fastq')

#print seqs

#Q4
from index import *

reads_k_mers = {}

for read in seqs:
    k_mers = Index(read,30).index
    for i in k_mers:
        reads_k_mers[i] = read
        

print len(reads_k_mers)
