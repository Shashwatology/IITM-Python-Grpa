
def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.

    Arguments:
    t: tuple - an even-length tuple.

    Return: tuple - a new tuple with the first half reversed.
    '''
    length = len(t)
    
    half = length // 2
    
    first_rev = t[0:half][::-1]
    
    final = first_rev + t[half:]
    
    return final
