'''
Created on 2012-10-03

@author: Janez Urevc
'''

import random
import time
import sys
from sorts import *

size = 10 if len(sys.argv) < 2 else int(sys.argv[1])
floor = -10000 if len(sys.argv) < 3 else int(sys.argv[2])
ceiling = 10000 if len(sys.argv) < 4 else int(sys.argv[3])
loops = 1 if len(sys.argv) < 5 else int(sys.argv[4])

def test_sorted(data):
    """Checks if a list is sorted and displays a warning if not.
    
    @type data: list
    @param data: Input list to be tested
    """
    for idx, val in enumerate(data):
        if idx > 0 and data[idx] < data[idx-1]:
            print "List not sorted:", data
            break
    


unsorted = [random.randint(floor, ceiling) for r in xrange(size)]

#print "Running sort algorithms on a list of", size, "elements between", floor, "and", ceiling

for i in range(1,loops):
    # Heap sort
    data = list(unsorted)
    start = time.time()
    heap_sort.heap_sort(data)
    print "Heap sort [s]:", (time.time() - start)
    test_sorted(data)
    #print data

    # Merge sort
    data = list(unsorted)
    start = time.time()
    data = merge_sort.merge_sort(data)
    print "Merge sort [s]:", (time.time() - start)
    test_sorted(data)
    #print data

    # Quicksort
    data = list(unsorted)
    start = time.time()
    quicksort.quicksort(data, 0, len(data)-1, False)
    print "Quicksort [s]:", (time.time() - start)
    test_sorted(data)
    #print data

    # Randomized Quicksort
    data = list(unsorted)
    start = time.time()
    quicksort.quicksort(data, 0, len(data)-1)
    print "Randomized Quicksort [s]:", (time.time() - start)
    test_sorted(data)
    #print data
