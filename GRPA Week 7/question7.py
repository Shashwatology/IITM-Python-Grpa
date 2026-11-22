
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    passage = " ".join(passage.split("\n"))
    letters = []
    
    for i in passage.split(" "):
        if i == "":
            continue
        else:
            letters.append(i.lower()[0])
        

    count = 0
    dic = {}
         
    for i in set(letters):
        count = 0
        for j in letters:
            if i == j:
                count = count + 1
        dic[count] = i

    value = [] 
    for i in dic.keys():
        value.append(i)

    top = sorted(value)[::-1][0]
    
    return dic[top]
