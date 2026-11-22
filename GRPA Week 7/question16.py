


def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    num = list(str(num))
    sent = []
    for i in num:
        if i == "1":
            sent.append("one")
        elif i == "2":
            sent.append("two")
        elif i == '3':
            sent.append("three")
        elif i == '4':
            sent.append("four")
        elif i == '5':
            sent.append("five")
        elif i == '6':
            sent.append("six")
        elif i == '7':
            sent.append("seven")
        elif i == '8':
            sent.append("eight") 
        elif i == '9':
            sent.append("nine")
        elif i == "0":
            sent.append("zero")
    
    return "-".join(sent)
