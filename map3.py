import sys
import numpy as np
size=0
no_of_node = int(sys.argv[1])
file = sys.argv[2]
f = open(file,"r")
Rank = np.ones((no_of_node));

# contents = f.read().split('\n')
for content in f:
		# print(content)
		a , b = content.strip().split();
		a= int(a)
		b = float(b)
		Rank[a-1] = b ;
# print(content)
# print(Rank)
for line in sys.stdin:
    
    line = line.strip()
    # print(line)
    i, j, value = line.split('\t', 2)
    i = int(i)
    j = int (j)
    # print(Rank[j])
    temp = float(value) * float(Rank[j])
    print ('%04d\t%f' % (i,temp))



    
