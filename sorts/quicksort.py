'''
Created on 1. nov. 2012

@author: slashrsm
'''

import random

def partition(data, p, r):
    """Partition step in Quicksort.
    
    @type data: list
    @type p: int
    @type r: int
    @param data: Input list to be sorted
    @param p: Start of the (sub)list
    @param r: End of the (sub)list
    @rtype: int
    @return: Index of dividing element of two partitions.
    """
    
    x = data[r]
    i = p - 1
    for j in xrange(p, r):
        if data[j] <= x:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[r] = data[r], data[i+1]
    return i + 1

def rand_partition(data, p, r):
    """Improves Quicksort performance randomizing pivot.
    
    @type data: list
    @type p: int
    @type r: int
    @param data: Input list to be sorted
    @param p: Start of the (sub)list
    @param r: End of the (sub)list
    @rtype: int
    @return: Index of dividing element of two partitions.
    """
    i = random.randint(p, r)
    data[r], data[i] = data[i], data[r]
    return partition(data, p, r)
    
def quicksort(data, p, r, rand = True):
    """Sorts a list using the Quicksort algorithm.
    
    @type data: list
    @type p: int
    @type r: int
    @param data: Input list to be sorted
    @param p: Start of the (sub)list
    @param r: End of the (sub)list
    """
    
    part = rand_partition if rand else partition
    
    if p < r:
        q = part(data,p,r)
        quicksort(data, p, q-1, rand)
        quicksort(data, q+1, r, rand)