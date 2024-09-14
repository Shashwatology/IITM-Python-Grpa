'''
Problem 1 - Data types - GRADED
Implement all the given functions according to the docstrings. There will be 6 function and 6 test cases corresponding to each of the functions.'''

#answer 

def loss_percent(bp, sp):
    """Find the loss percentage given the buying price and the selling price.
    Args:
    bp (int): The buying price.
    sp (int): The selling price.
    Returns:
    float: The loss percentage.
    Examples:
    >>> loss_percent(10, 8)
    20.0
    >>> loss_percent(20, 15)
    25.0
    """
    loss = (bp-sp)
    loss_percent = (loss/bp)*100
    return loss_percent

def swap_first_and_last_chars(s):
    '''Swap the first and last characters of a string.
    Args:
    s (str): The input string.
    Returns:
    str: The string with first and last characters swapped.
    Examples:
    >>> swap_first_and_last_chars("hello")
    'oellh'
    >>> swap_first_and_last_chars("world")
    'dorlw'
    '''
    swapping_str = s[-1] + s[1:-1] + s[0]
    return swapping_str


def add_first_three_items_to_the_last(l):
    '''Add the first three elements to the 
    end of the list in the same order. 
    Modify the list inplace
    Args:
    l (list): The input list.
    Returns:
    None.
    Examples:
    >>> lst = [1, 2, 3, 4, 5]
    >>> add_first_three_items_to_the_last(lst)
    >>> lst
    [1, 2, 3, 4, 5, 1, 2, 3]
    '''
    l.extend(l[:3])

    return l
    ...

def are_alternate_positions_equal(t):
    """Check if the elements at alternate positions in the tuple are equal.
    Assume even number of elements in the tuple.
    Args:
    t (tuple): The input tuple.
    Returns:
    bool: result as True or False
    Examples:
    >>> are_alternate_positions_equal([1, 2, 3, 4, 5, 6])
    False
    >>> are_alternate_positions_equal([1, 1, 2, 2, 3, 3])
    True
    """
    if t[0]==t[1] and t[2]==t[3] and t[4]==t[5]:
        return True
    else:
        return False

def has_all_values(l, s):
    '''Check if all numbers from a list are present in a set.
    Args:
    l (list): The input list of numbers.
    s (set): The input set of numbers.
    Returns:
    bool: result as True or False
    Examples:
    >>> has_all_values([1, 2, 3, 4, 4, 3, 2, 1], {1, 2, 3, 4})
    True
    >>> has_all_values([1, 2, 3, 1, 2, 3, 3], {2, 3})
    False
    '''
    if set(l) == s:
        return True
    else:
        return False

def swap_key_and_value(d, k):
    """Swap the key and value for a given key in a dictionary.
    Modify the dictionary inplace do not return a new dictionary.
    Args:
    d (dict): The input dictionary.
    k: The key to swap.
    Returns:
    dict: The dictionary with the key and value swapped.
    Examples:
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> swap_key_and_value(d,'b')
    >>> d
    {2: 'b', 'a': 1, 'c': 3}
    >>> d = {1: 'a', 2: 'b', 3: 'c'}
    >>> swap_key_and_value(d, 2)
    >>> d
    {1:'a', 'b': 2, 3: 'c'}
    """

    if k in d:
        value = d[k]  # Get the value for key k
        del d[k]      # Remove the key k from the dictionary
        d[value] = k
