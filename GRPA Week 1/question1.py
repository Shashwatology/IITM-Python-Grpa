'''
GrPA 1 - Numbers (Arithemetic) - GRADED
Solve the below tasks related to Numbers.
Tasks 1 to 3 - building up Arithemetic expression
Tasks 4 and 5 - floating point arithemetic
Tasks 6 and 7 - modulo and floor division
Problem Type: Input variable - Output Variable, Hidden suffix for evaluation
'''
#Solution - 

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470
# <eoi>

output1 = a + b # int: sum of a and b
output2 = 2 * (a + b) # int: twice the sum of a and b
output3 = abs(a - b )  # int: absolute difference between a and b
output4 = abs((a + b) - (a * b)) # int: absolute difference between sum and product of a and b

# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = price - (price * (discount_percent / 100)) # float

# Round the discounted_price
rounded_discounted_price = round(discounted_price) # int

# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = total_mins // 60 # int: hint: think about floor division operator
mins = total_mins % 60 # int