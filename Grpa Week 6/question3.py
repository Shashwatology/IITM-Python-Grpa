'''
GrPA 3 - Problem Solving - GRADED
Implement all the given functions according to the docstring. You may need to implement additional functions that will help you breakdown some of the problems into simpler ones.'''
#answer

def is_num_sorted(num) -> bool:
    num_str = str(num)
    return num_str == ''.join(sorted(num_str))
'''
    Check if a number is sorted.
    sorted means the digits of a number are sorted in ascending order.
    Eg. 1468 - sorted , 4948 - not sorted.
    Argument: num: int
    Return: bool
    '''


def sorted_num_count(nums: list) -> int:
    return sum(is_num_sorted(num) for num in nums)
'''
    Given a list of nums(int) find the count of sorted numbers in the list.
    Arguments: nums - list[int]
    Return: count - int
    '''

def common_substring(words: list) -> str:
    if not words:
        return None
    shortest = min(words, key=len)
    for word in words:
        if shortest not in word:
            return None
    return shortest
'''
    Given a list of words check whether there is a word in words 
    that is a substring of all other words.
    If there is a word return that word else return None
    Hint: only the smallest word can be a substring of all other words.
    Arguments: words - list[str]
    Return: common_substr_word - str
    '''


def is_valid_phone_number(phone_no: int) -> bool:
    phone_str = str(phone_no)
    if len(phone_str) != 10 or not phone_str.startswith('98123'):
        return False
    return all(phone_str.count(digit) <= 5 for digit in set(phone_str))
'''
    Check if a number is valid for a specific operator.
    A phone number is valid if 
        - it has 10 digits
        - should begin with 98123
        - same digit should not occur more that 5 times.
    '''

def validate_phone_numbers(phone_nos: list) -> dict:
    return {phone: "VALID" if is_valid_phone_number(phone) else "INVALID" for phone in phone_nos}
'''
    Given a list of phone numbers, create a dict with 
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.
    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]
    '''


def get_election_winner(votes: dict) -> str:
    return max(votes, key=votes.get)
'''
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes
    Arguments: votes - dict[str, int]
    Return: winner - str
    '''

def misspelt_words(vocab: str, sentence: str) -> list:
    vocab_set = set(vocab.split(','))
    return [word for word in sentence.split() if word not in vocab_set]
'''
    Given a comma separated string of vocabulary, 
    and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.
    The words which are not in the vocabulary are considered misspelt.
    Arguments: 
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list
    '''

def count_sock_pairs(sock_colors: list) -> int:
    from collections import Counter
    return sum(count // 2 for count in Counter(sock_colors).values())
'''
    Given a list of sock colors representing the color of each sock, 
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"] 
    2 red+ 1 green+ 1 blue = 5 pairs
    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    '''

def is_vowely(word: str) -> bool:
    vowels = 'aeiou'
    word_vowels = ''.join(char for char in word.lower() if char in vowels)
    return word_vowels == vowels
'''
    Check if a given word is vowely. A word is vowely if 
    - it has all the vowels in it.
    - the vowels occur in ascending order.
    Assume no letter repeats in the given word.
    Eg. abecidofu - vowely, tripe - not vowely, eviaoqu - not vowely
    Argument: word - a string with no letter repeated
    Return: bool 
    Hint: if the non-vowels are removed from the word, it would be just aeiou
    '''

def vowely_count(words: list) -> int:
    return sum(is_vowely(word) for word in words)
'''
    Given a list of words find the number of vowely words from the list.    
    Arguments: words :list[str]
    Return: int - number of vowely words
    '''


def format_name(first: str, middle: str, last: str) -> str:
    if middle:
        return f"{first.capitalize()} {middle.capitalize()} {last.capitalize()}"
    return f"{first.capitalize()} {last.capitalize()}"
'''
    Given three lower case parts of name, 
    return the full name with first letter capitalized in each part.
    Note that middle name can be empty.
    '''


def double_palindromes(n: int) -> list:
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    return [i for i in range(1, n+1) if is_palindrome(i) and is_palindrome(i**2)]
'''
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if 
    it is a palindrome and its square is a palindrome.
    Eg. 
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome
    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    '''


def scores_spx(kakashi_moves:list, guy_moves:list):
  k_score = 0
  g_score = 0
  for i in range(len(kakashi_moves)):
    if kakashi_moves[i] == "S" and guy_moves[i] == "X" or kakashi_moves[i] == "X" and guy_moves[i] == "P" or kakashi_moves[i] == "P" and guy_moves[i] == "S":
      k_score += 1
    elif kakashi_moves[i] == guy_moves[i]:
      continue
    else:
      g_score += 1
  return k_score, g_score
'''
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X
    Arguments: 
    kakashi_moves and guy_moves - list of moves where each move 
        is a string corresponding to the symbol
    Return: kakashi_score:int , guy_score:int
    '''