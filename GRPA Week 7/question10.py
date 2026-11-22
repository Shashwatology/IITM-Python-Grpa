

def delete_first_three(l: list) -> None:
    '''
    Given a list, delete the first three elements in the list.

    Arguments:
    l: list - a list of elements.

    Return: None - the list is modified in place.
    '''
    if len(l) <= 3:
        for _ in range(len(l)):
            l.pop(0)
        return l
    else:
        l.pop(0)
        l.pop(0)
        l.pop(0)
        
        return l
    
