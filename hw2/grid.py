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

'''
You had a wonderful idea of making printHorizontal and printVertical functions,
but you could also take it a step further and generalize the script (lines 12-26)
and make a function draw_grid that lets me print an nxn grid.
'''