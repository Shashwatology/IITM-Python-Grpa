
def create_indexed_dict(items: list) -> dict:
      '''
    Given a list of items, create a dictionary with the indices as keys and the items as items.
    
    Args: items (list): A list of items.

    Returns:
        dict: A dictionary with indices as keys and items as items.
    '''
    dic = {}
    for i,j in enumerate(items):
        dic[i] = j 
    
    return dic
