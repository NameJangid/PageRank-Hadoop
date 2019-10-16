
from operator import itemgetter
import numpy as np
import sys
# import sys

current_outlink = []
current_node = None
no_of_node = int(sys.argv[1])

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    first, second = line.split('\t', 1)


    # convert count (currently a string) to int
    first = int(first)
    second = int(second)
    if(first == current_node):
        current_outlink.append(second)
    else:
        if(current_node!=None):
            print('%04d'%(current_node), end="\t")
            for k in range(0,len(current_outlink)):
                print ('%04d' % (current_outlink[k]), end=" ")
            print("")
        current_node = first        
        current_outlink = []
        current_outlink.append(second)
        

if current_node == first:
    print('%04d'%(first), end="\t")
    for k in range(0,len(current_outlink)):
        print ('%04d' % (current_outlink[k]), end=" ")
    print("")
    # print ('%s\t%s' % (i, current_outlink))

# if(i == no_of_node):
#     current_outlink=[]
#     print ('%s\t%s' % (i, current_outlink))
