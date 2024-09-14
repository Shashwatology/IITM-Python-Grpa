'''
GrPA 4 - Function Basics - GRADED
You are required to complete the following functions to perform various operations on tuples and lists.
swap_halves: Swap the first and second halves of a tuple with an even length.
Input: A tuple of even length.
Output: A new tuple where the first and second halves are swapped.
swap_at_index: Break a tuple at a given index ( k ) (the element at the ( k )-th index is included in the first half before swapping) and swap the parts.
'''

#answer 

def swap_halves(items):
    mid = len(items) // 2
    return items[mid:] + items[:mid]

def swap_at_index(items, k):
    return items[k+1:] + items[:k+1]

def rotate_k(items, k=1):
    k = k % len(items) 
    return items[-k:] + items[:-k]

def first_and_last_index(items, elem):
    first = items.index(elem)
    last = len(items) - 1 - items[::-1].index(elem)
    return (first, last)

def reverse_first_and_last_halves(items):
    mid = len(items) // 2
    items[:mid] = reversed(items[:mid])
    items[mid:] = reversed(items[mid:])