#written by neal s.  no license.

from math import *

def printHorizontal():
    print '+ - - - - + - - - - +'

def printVertical():
    print '|         |         |'


n = 0
    
printHorizontal()
n+=1

while (n<11):
    if ((n%5) == 0):
        printHorizontal()
        
    else:
        printVertical()
    
    n+=1

print "Done"        
