def readGenome(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                data.append(line.rstrip())
    return data



def find_spliced_motif(s1, read):
	motif = []	
	k = -1
	for i in xrange(0,len(s1)):		
		for j in xrange(k+1,len(read)):
			if(s1[i] == read[j]):
				motif.append(str(j+1))
				k = j
				break
	return motif


data = readGenome('rosalind_input.txt')

print data[0]

print ' '.join(find_spliced_motif(data[1],data[0]))
