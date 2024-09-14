'''
Question - 
GrPA 2 - Numbers (Relational and Logical) - GRADED
Solve all the below tasks related to relational and logical operators.
This exercise gives you practice in building up boolean expressions.
'''

#Answer - ;

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

# Assume discount is given in percentages

# <eoi>

output1 = (a >= 5) # bool: True if a greater than or equal to 5

output2 = ( a % 5 == 0 ) # bool: True if a is divisible by 5

output3 = ( a % 2 != 0 and a < 10 ) # bool: True if a is odd number less than 10

output4 = ( a % 2 != 0 and -10 < a < 10 ) # bool: True if a is an odd number within the range -10 and 10

output5 = (len(str(a)) % 2 == 0 and len(str(a)) <= 10 ) # bool: True if a has even number of digits but not more than 10 digits

is_offer1_cheaper = ( price1 * (1 - discount1 / 100) < price2 * (1 - discount2 / 100) ) # bool: True if the offer1 is strictly cheaper