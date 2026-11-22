

def remove_edges(s: str) -> str:
    '''
    Return a new string with the first two and last two 
    characters removed from the given string. 

    Arguments:
    s: str - a string.

    Return: str - a string with first and last two characters removed.
    '''
    if len(s) <= 4:
        return ""
    else:
        return s[2:-2]
    

