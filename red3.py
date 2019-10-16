import sys
import numpy as np
current_node = None
current_rank = 0
# file = sys.argv[2]
current_rank = float(current_rank)
for line in sys.stdin:
    
    line = line.strip()
    # print(line)
    i, value = line.split('\t', 1)
    i = int (i)
    # print(value)
    value = float(value)

    if(i==current_node):
        current_rank +=value
    else:
        if(current_node!=None):
            print ('%04d\t%f' % (current_node+1,current_rank));
        current_node = i
        current_rank = value


if(current_node == i):
    print ('%04d\t%f' % (current_node+1,current_rank));



    
