# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Neal S.
"""

# import random_art
# reload(random_art)

from random import *
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
    """Recursively evaluates the string of functions that is passed to it for the point x,y.
     Takes three inputs.  The first input is the random function to evaluate (which will be generated using build_random_function).  
     The second input is the value of x to evaluate the function at (this will allow you to evaluate the function ["x"] when you encounter it in the random function).  
     The third input is the value of y to evaluate the function at (analogously to the role of the input x, 
     the input y will allow you to evaluate the function ["y"] when you encounter it in the random function). 
     The output of this function is the value of the input function evaluated at the input (x,y) pair.
    """
    if f[0] == "x":
        return float(x)
    elif f[0] == "y":
        return float(y)
    else:         
        if f[0] == "prod": 
            prod1 = evaluate_random_function(f[1], x, y)
            prod2 = evaluate_random_function(f[2], x, y)
            return prod1*prod2
        elif f[0] == "cos_pi":
            return math.cos(pi*evaluate_random_function(f[1], x, y))
        elif f[0] == "sin_pi":
            return math.sin(pi*evaluate_random_function(f[1], x, y))
        elif f[0] == "sqrt":
            return (evaluate_random_function(f[1], x, y))#**.5
        elif f[0] == "cos_pi":
            return math.cos(pi*evaluate_random_function(f[1], x, y))            
        elif f[0] == "sinh_pi":
            return math.sin(pi*evaluate_random_function(f[1], x, y)) #/ evaluate_random_function(f[1], x, y))

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        Gets the constant of proportionality by applying the slope formula: (y2-y1)/(x2-x1),
        gets rid of the values input offset, and shifts it up by the output interval's beginning offset.
    """
    proportion = (output_interval_end - output_interval_start) / (input_interval_end - input_interval_start)
    return proportion * (val - input_interval_start) + output_interval_start
 

if __name__ == '__main__':
    
    image_size = 350, 350
    image = Image.new("RGB", image_size)
    
    
    red_channel = build_random_function(randint(1, 7), randint(4, 12))
    green_channel = build_random_function(randint(1, 7), randint(4, 12))
    blue_channel = build_random_function(randint(1, 7), randint(4, 12))

    for i in range(image_size[0]):  #loop across x axis of image
        for j in range(image_size[1]):  #loop down y axis of image
            x = remap_interval(i, 0.0, image_size[0], -1.0, 1.0)    #create values for to evaluate the function at an x-y point.
            y = remap_interval(j, 0.0, image_size[1], -1.0, 1.0)
            
            red_value = int(remap_interval(evaluate_random_function(red_channel, x, y), -1.0, 1.0, 0.0, 255))
            green_value = int(remap_interval(evaluate_random_function(green_channel, x, y), -1.0, 1.0, 0.0, 255))
            blue_value = int(remap_interval(evaluate_random_function(blue_channel, x, y), -1.0, 1.0, 0.0, 255))
            
            image.putpixel((i, j), (red_value, green_value, blue_value))

    image.save("output10.bmp")
    image.show()
    
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
