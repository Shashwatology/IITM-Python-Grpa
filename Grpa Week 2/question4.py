'''
Question 
GrPA 4 - Conditionals - Applications - GRADED
Problem Type: Standard Output - Standard Output
You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.
'''

#answer 

operation = input()

if operation == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")
elif operation == "perfect_square_check":
    number = int(input())
    import math
    if math.sqrt(number) == int(math.sqrt(number)):
        print("yes")
    else:
        print("no")
elif operation == "vowel_check":
    text = input()
    if any(char in "aeiouAEIOU" for char in text):
        print("yes")
    else:
        print("no")
elif operation == "divisibility_check":
    number = int(input())
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 2 == 0:
        print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")
elif operation == "palindrominator":
    text = input()
    print(text + text[::-1][1:])
elif operation == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = (principal_amount * interest_rate * n_years)
    print(round(simple_interest))
else:
    print("Invalid Operation")

print(f"{total_cost:.02f}") # type: ignore