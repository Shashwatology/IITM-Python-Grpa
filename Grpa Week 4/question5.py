'''GrPA 5 - Comprehensions - GRADED
This will help you build up the basics of list comprehensions.
sum_of_squares - find the sum of squares of numbers in a list - (mapping and aggregation)
total_cost - given quantitiy and price of each item as a list of tuples find the total cost using list comprehensions
abbreviation - given a string with multiple words seperated by space, form an abbrevation out of it by taking the first letter in caps. (mapping and aggregation)
palindromes - given a list of strings, create a new list with only palindromes filtering
all_chars_from_big_words - find the all unique characters (case insensitive, make all lowercase) from all words with size greater than 5 in a given sentence with words seperated by spaces. (filtering)
flatten - flatten a nested list using comprehension
unflatten - given a flat list and number of rows, create a matrix (2d list) with that number of rows. (nested-aggregation)
make_identity_matrix - make an identity (with ones on the main diagonal and zeros elsewhere) given the size.
make_lower_triangular_matrix - given number of rows m, create a lower triangular matrix like the pattern below. for m = 5
[
  [1,0,0,0,0],
  [1,2,0,0,0],
  [1,2,3,0,0],
  [1,2,3,4,0],
  [1,2,3,4,5]
]
Note: you cannot use if statements or loops withing the functions.'''

#answer 
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

def total_cost(cart):
    return sum(quantity * price for quantity, price in cart)

def abbreviation(sentence):
    return '.'.join(word[0].upper() for word in sentence.split()) + '.'

def palindromes(words):
    return [word for word in words if word == word[::-1]]

def all_chars_from_big_words(sentence):
    return set(char.lower() for word in sentence.split() if len(word) > 5 for char in word)

def flatten(lol):
    return [item for sublist in lol for item in sublist]

def unflatten(items, n_rows):
    return [items[i:i + len(items) // n_rows] for i in range(0, len(items), len(items) // n_rows)]

def make_identity_matrix(m):
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

def make_lower_triangular_matrix(m):
    return [[j + 1 if j <= i else 0 for j in range(m)] for i in range(m)]