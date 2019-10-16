
from operator import itemgetter
import numpy as np
import sys

current_col = 0;
no_of_node = int(sys.argv[1])
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    first, second = line.split('\t', 1)
    
    # print(second[0])
    # print(len(second))
    # convert count (currently a string) to int
    first = int(first)
    # second = int(second)
    # link=[]
    link = second.split()
    # print(len(link))
    

    while(first!=current_col):
        for i in range (0,no_of_node):
            d = (0.85 * 1/no_of_node) + ((1-0.85)/no_of_node)
            print ('%04d\t%04d\t%s' % (i,current_col,d))
        current_col+=1;

    # j=0

    for i in range (0,no_of_node):
        check=0
        for j in range (0,len(link)):
            if(i == int(link[j])):
                d = (0.85 * 1/len(link)) + ((1-0.85)/no_of_node)
                print ('%04d\t%04d\t%s' % (i,current_col,d)) 
                check =1
        if(check==0):
            d = (0.85 * 0) + ((1-0.85)/no_of_node)         
            print ('%04d\t%04d\t%s' % (i,current_col,d))

            # if(j<len(link) and i == int(link[j])):
                
            #     # print ('{:04d}\t{:04d}\t{}'.format(i,current_col,1/len(link)))
            #     j+=1;
            # else:
            #     d = (0.85 * 0) + ((1-0.85)/no_of_node)                
            #     print ('%04d\t%04d\t%s' % (i,current_col,d))
            #     # print()
    



    current_col+=1

    

while(current_col<no_of_node):
    for i in range (0,no_of_node):
        d = (0.85 * 1/no_of_node) + ((1-0.85)/no_of_node)
        print ('%04d\t%04d\t%s' % (i,current_col,d))
        # print ('%04d\t%04d\t%s' % (i,current_col,1/no_of_node))
    current_col+=1




        # else:
        #     if(i+1==link[j] and i!=current_col):
        #         print ('%s\t%s\t%s' % (i,current_col,1/len(second)))
        #         j+=1
        #     else:
        #         print ('%s\t%s\t%s' % (i,current_col,0))







#     if current_node == first:
#         current_outlink.append(second)
#     else:
#         print ('%s\t%s' % (current_node, current_outlink))
#         current_node = first
#         current_outlink = []
#         current_outlink.append(second)

# if current_node == first:
#     print ('%s\t%s' % (current_node, current_outlink))