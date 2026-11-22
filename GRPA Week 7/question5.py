
def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    num = []
    word = []
    
    for i in range(len(list(string))):
        if i % 2 == 0:
            num.append(string[i])
        else:
            word.append(string[i]) 
    
    num = "".join(num)

    word = "".join(word)
    
    if num.isdigit() and word.isalpha() :
        return True
    else:
        return False
        
