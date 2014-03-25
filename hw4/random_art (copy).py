# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# import random_art
# reload(random_art)

# you do not have to use these particular modules, but they may help
from random import * #randint
import Image
import math

pi = 3.14159

def build_random_function(min_depth, max_depth):
    """
    Makes a random function comprising random compositions of the following functions:
    prod(a,b) = ab
    cos_pi(a) = cos(pi*a)
    sin_pi(a) = sin(pi*a)
    sqrt(a) = a**.5
    sinh_pi(a) = sinh(pi*a)
    x(a,b) = a
    y(a,b) = b
    The input min_depth specifies the minimum amount of nesting for the function that you generate.  
    The input max_depth specifies the maximum amount of nesting of the function that you generate
    """
    if max_depth == 1:
        print "done"        
        return ["x"] if random() < 0.5 else ["y"]
    else:
        case = randint(0,6)
        if case == 6:
            prod1 = build_random_function(min_depth-1, max_depth-1)
            prod2 = build_random_function(min_depth-1, max_depth-1)
            res = ["prod"]
            res.append(prod1)
            res.append(prod2)
            return res
        elif case == 5:
            a = build_random_function(min_depth-1, max_depth-1)
            return ["cos_pi"] + [a]
        elif case == 4:
            a = build_random_function(min_depth-1, max_depth-1)
            return ["sin_pi"] + [a]
        elif case == 3:
            a = build_random_function(min_depth-1, max_depth-1)
            return ["sqrt"] + [a]
        elif case == 2:
            a = build_random_function(min_depth-1, max_depth-1)
            return ["sinh_pi"] + [a]
        elif case == 1:
            return ["y"]
        elif case == 0:
            return ["x"]
    
def evaluate_random_function(f, x, y):
    # your doc string goes here
    print "in eval"
    if f[0] == "x":
        return float(x)
    elif f[0] == "y":
        return float(y)
    else:        
        print "in else"
        print f[0]
        if f[0] == "prod": 
            print "in prod"
            prod1 = evaluate_random_function(f[1], x, y)
            print prod1
            prod2 = evaluate_random_function(f[2], x, y)
            print prod2
            return prod1*prod2
        elif f[0] == "cos_pi":
            return math.cos(pi*evaluate_random_function(f[1], x, y))
        elif f[0] == "sin_pi":
            return math.sin(pi*evaluate_random_function(f[1], x, y))
        elif f[0] == "sqrt":
            return (evaluate_random_function(f[1], x, y))**.5
        elif f[0] == "cos_pi":
            return math.cos(pi*evaluate_random_function(f[1], x, y))            
        elif f[0] == "sinh_pi":
            return math.sin(pi*evaluate_random_function(f[1], x, y) / evaluate_random_function(f[1], x, y))
