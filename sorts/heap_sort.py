'''
Created on 2012-10-30

@author: Janez Urevc
'''

def shift_down(data, start, end):
    """Given an element in a heap shifts it down towards the
    leafs to ensure correct heap structure (direct children should
    always be smaler than the parent)
    
    @type data: list
    @type start: Integer
    @param data: heap represented as a list
    @param start: node ID to start with
    """
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if data[swap] < data[child]:
            swap = child
        if child+1 <= end and data[swap] < data[child+1]:
            swap = child+1
        if swap != root:
            data[swap], data[root] = data[root], data[swap]
            root = swap
        else:
            return
        
def shift_up(data, start, end):
    """Given an element in a heap shifts it up towards the
    root to ensure correct heap structure (direct children should
    always be smaler than the parent)
    
    @type data: list
    @type start: Integer
    @param data: heap represented as a list
    @param start: node ID to start with
    """
    child = end
    while child > start:
        parent = (child - 1) / 2
        if data[parent] < data[child]:
            data[parent], data[child] = data[child], data[parent]
            child = parent
        else:
            return
    

def heapify(data):
    """Transforms a list into a heap.
    
    @type data: list
    @param data: Input list
    """
    #start = (len(data) - 2) / 2
    #while start >= 0:
    #    shift_down(data, start, len(data) - 1)
    #    start -= 1
    
    end = 1
    while end < len(data) - 1:
        shift_up(data, 0, end)
        end += 1


def heap_sort(data):
    """Sorts a list using the Heapsort algorithm.
    
    @type data: list
    @param data: Input list
    """ 
    heapify(data)
    
    end = len(data) - 1
    while end > 0:
        data[end], data[0] = data[0], data[end]
        end -= 1
        shift_down(data, 0, end)
