'''
Problem 2 - Data Processing - GRADED
Given a list of integers, find the number of hostile_pairs in the given list.
Two positive integers are called hostile if they have no common digits.'''

#answer 
def n_hostile_pairs(L:list)->int:
    '''
    Given a list of integers, find the number of 
    hostile_pairs in the given list.
    Two positive integers are called hostile 
    if they have no common digits. 
    Args:
        L: list[int] - numbers to check
    Return:
        int - number of hostile pairs
    '''
    hostile_pairs = 0
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if not set(str(L[i])) & set(str(L[j])):
                hostile_pairs += 1
    return hostile_pairs

