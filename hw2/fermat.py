#written by neal s.  no license.
def check_fermat(a, b, c, n):
    
    if (n > 2):
        if ( (a**n + b**n) == c**n ):
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn't work."
    else:
        print "Error!  n must be greater than 2"
            
            
def more_money_more_problems():
    print "This program checks Fermat's last theorum,"
    print "\nseeing if a^n + b^n = c^n"
    print "\nfor values of n greater than 2."
    print "Please enter a value for a"
    a = int(raw_input())
    print "Please enter a value for b"
    b = int(raw_input())
    print "Please enter a value for c"
    c = int(raw_input())
    print "Please enter a value for n"
    n = int(raw_input())
    print "Checking..."
    check_fermat(a, b, c, n)
    
    
            
more_money_more_problems()
