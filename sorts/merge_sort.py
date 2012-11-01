'''
Created on 2012-10-30

@author: Janez Urevc
'''

def merge(left, right):
    """Merges left and right sub-lists in Mergesort.
    
    @type left: list
    @type right: list
    @param left: left sub-list
    @param right: right sub-list
    @rtype list
    @return merged list, containing (sorted) elements from both left and right
    """
    result = []
    i = j = 0
    while i < len(left)-1 or j < len(right)-1:
        if i < len(left)-1 and j < len(right)-1:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left)-1:
            result.extend(left[i:])
            break
        elif j < len(right)-1:
            result.extend(right[j:])
            break
    return result

def merge_sort(data):
    """Sorts a list using the Mergesort algorithm.
    
    Divides the list in two sublists and recursively executes
    Mergesort on both of them.
    
    @type data: list
    @param data: Input list
    @rtype: list
    @return: Sorted list
    """
    if len(data) == 1:
        return data
    
    middle = len(data)/2
    left = merge_sort(data[0:middle])
    right = merge_sort(data[middle:])
    
    return merge(left, right)
