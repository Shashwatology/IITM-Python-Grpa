'''
GrPA 1 - Dictionary Basics - GRADED
You are tasked with implementing a series of functions that perform various operations on dictionaries in Python. These functions will manipulate dictionaries that represent fruit prices and perform different operations as specified.
dictionary_operations(fruit_prices: dict, fruits: list)
'''

#answer 

def dictionary_operations(fruit_prices:dict, fruits:list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    order_print(fruit_prices) # type: ignore # this function is in the hidden code 

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2
    order_print(fruit_prices) # type: ignore

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2
    order_print(fruit_prices) # type: ignore

    # delete both key and value for fruits[3] from fruit_prices
    del fruit_prices[fruits[3]]
    order_print(fruit_prices) # type: ignore

    # print the price of fruits[4]

    print(fruit_prices[fruits[4]])

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(sorted(fruit_prices.keys()))

    # print the prices of the fruits as a list sorted in ascending order.
    print(sorted(fruit_prices.values()))

def increase_prices(fruit_prices:dict) -> None:
    '''
    Increase the prices of every fruit by 20 percent and round to two decimal places
    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    Return:
    None - Do not return any thing - modify inplace
    '''
    for fruit in fruit_prices:
        fruit_prices[fruit] *= 1.2 
        fruit_prices[fruit] = round(fruit_prices[fruit] , 2)

def dict_from_string(string:str,key_type,value_type):
    '''
    Given a string where each line has a comma seperated key-value pair, create a dictionary out of it. Also convert the types of key and values to the given types.
    Arguments:
    string - str: string to be parsed
    key_type - class: the data type of the keys
    value_type - class: the data type of the values
    Return:
    D - dict: the output dictionary
    '''
    D = {}
    for line in string.split("\n") :
        key , value = line.split(",")
        D[key_type(key)] = value_type(value)
    return D

def dict_to_string(D:dict) -> str:
    '''
    Convert the given dictionary back to the string fromat produced by dict_from_string. Again, do not use loops or conditionals, use comprehensions.
    '''
 #{'Apple': 2, 'Banana': 3, 'Grapes': 3, 'Orange': 4, 'Papaya': 5}
    return "\n".join(str(key)+ ","+str(value) for key,value in D.items())