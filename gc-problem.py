from __future__ import division
def readRosalindFile(filename):
    dict = {}
    read = ''
    with open(filename, 'r') as f:
        for line in f:
        	if line[0] == '>':
        		key = line[1:len(line)-1] 
        		dict[key] = ''
        		continue
        	else:
        		dict[key] += line[0:len(line)-1]        	        	
    return dict

def findGCByPos(dict):
    gc = 0
    max = 0
    max_key = ''
    for key in dict.keys():
        for i in range(len(dict[key])):
            if dict[key][i] == 'C' or dict[key][i] == 'G':
                gc += 1
        if gc > max:
       	 max = gc
       	 max_key = key      
        gc = 0
    return max_key, max

dict = readRosalindFile('rosalind_lexf.txt')

key, gc = findGCByPos(dict)

print key
print  (gc/len(dict[key]))*100