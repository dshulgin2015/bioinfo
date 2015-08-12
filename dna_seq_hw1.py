def naive_with_rc(p, t):
    occurrences = []
    p_rev = reverseComplement(p);
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match, match_rev = True, True
        for j in range(len(p)): # loop over characters
            if t[i+j] != p[j]: # compare characters of p
                match = False
            if t[i+j] != p_rev[j]:  # compare characters reverse complement if p
                match_rev = False
            if(not (match or match_rev)):
                break
        if match or match_rev:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def leftmost_occur(p, t):
    occurrences = []
    p_rev = reverseComplement(p);
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match, match_rev = True, True
        for j in range(len(p)): # loop over characters
            if t[i+j] != p[j]: # compare characters of p
                match = False
            if t[i+j] != p_rev[j]:  # compare characters reverse complement if p
                match_rev = False
            if(not (match or match_rev)):
                occurrences.append(i)
                break
        if match or match_rev:
            return i  # all chars matched; record
    return occurrences


def naive_2mm(p, t):
    occurrences = []
    match = True
    counter = 0;
    for i in range(len(t) - len(p) + 1):  # loop over alignments
     
        for j in range(len(p)):  # loop over characters
            
            if t[i+j] != p[j]:  # compare characters
                counter += 1 

            if counter > 2:
                match = False
                break
                           
        if match:
            occurrences.append(i) # all chars matched; record
        match = True
        counter = 0

    return occurrences

def leftmost_occur_2mm(p, t):
    occurrences = []
    
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        counter = 0;
        match = True
        for j in range(len(p)):  # loop over characters
             if(counter > 2):
                match = False
                break
             if t[i+j] != p[j]:  # compare characters
                counter = counter + 1                           
        if match:
            occurrences.append(i)
            break # all chars matched; record

    return occurrences


def phred33ToQ(qual):
    return ord(qual) - 33

def createHist(qualities):
    # Create a histogram of quality scores
    hist = [0]*50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist


# Plot the histogram
import matplotlib.pyplot as plt
#plt.plot(range(len(h)), h)
#plt.show()

def findGCByPos(reads):
    ''' Find the GC ratio at each position in the read '''

    # Keep track of the number of G/C bases and the total number of bases at each position
    gc = [0] * 100
    totals = [0] * 100
    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            totals[i] += 1
    
    # Divide G/C counts by total counts to get the average at each position
    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])

    return gc



#genome = readGenome('lambda_virus (1).fa')

#print len(naive_with_rc('AGGT', genome)) # Q1
#print len(naive('TTAA', genome)) #Q2
#print leftmost_occur('ACTAAGT', genome)#Q3
#print leftmost_occur('AGTCGA', genome)#Q4
#print  len(naive_2mm('TTCAAGCC',genome))
#print leftmost_occur_2mm('AGGAGGTT', genome)[0]#Q6

#seqs, quals = readFastq('ERR037900_1.first1000.fastq')

#h = createHist(quals)

#plt.plot(range(len(h)), h)
#plt.show()

#gc = findGCByPos(seqs)
#for i in range(60,70):
#    if gc[i] == 0.055:
#       print i
#plt.plot(range(len(gc)), gc)
#plt.show()



