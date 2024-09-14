'''
Problem 3 - Data Processing - GRADED
Given a list of words, check if all the words are anagrams. Assume words are lowercase.
Two words are anagrams of each other if each word can be obtained by rearranging the letters in the other word.'''

#answer 

def are_anagrams(words:list)->bool:
    '''
    Check if all the given words are anagrams.
    Args: words - list[str]: list of lowercase words
    Return: bool - True if all the words are anagrams, else False.
    '''

    if not words:
        return True
        sorted_first_word = sorted(words[0])
    for word in words[1:]:
        if sorted(word) != sorted_first_word: # type: ignore
            return False

    return True