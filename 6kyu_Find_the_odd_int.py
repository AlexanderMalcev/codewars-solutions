"""
 Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times. 
"""


#solution
def find_it(seq):
      for x in seq:
          if seq.count(x)%2 != 0:
              return x