def boyer_moore(p, p_bm, t):
    """ Do Boyer-Moore matching. p=pattern, t=text,
        p_bm=BoyerMoore object for p """
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences

#Question 1: How many alignments does the naive exact matching algorithm 
#            try when matching the string GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG (derived from human Alu sequences)
#            to the excerpt of human chromosome 1?
from dna_seq_hw1 import readFastq, readGenome

genome = readGenome('chr1.GRCh38.excerpt.fasta')

alignments = len(genome) - len('GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG') + 1

print alignments

#Question 1: How many character comparisons does the naive exact matching algorithm 
#            try when matching the string GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG (derived from human Alu sequences)
#            to the excerpt of human chromosome 1?
print alignments * len('GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG')

from bm_preproc import *

# GCTAGCTCTACGAGTCTA
p = 'TCAA'
p_bm = BoyerMoore(p, alphabet='ACGT')
print p_bm.bad_character_rule(2, 'T')
