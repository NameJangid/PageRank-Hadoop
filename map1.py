import sys

for line in sys.stdin:
    
    line = line.strip()
    # print(line)
    words = line.split()

    # print(words)
    print ('%04d\t%04d' % (int(words[0])-1, int(words[1])-1))