

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    ...
    
    length = len(s)
    half = length // 2
    
    first_half = s[:half]
    second_half = s[half:] 
    
    for i in second_half:
        if i == "A" or i == "a":
            return True
    
    return False
