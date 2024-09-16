"""
Question 
GrPA 5 - Conditionals - Debugging - GRADED
Problem Type: Standard Input - Standard Output, Debugging, and missing
How to solve: To solve this problem use the Python tutor button. Paste the template(buggy) code in the python tutor, you can also include the sample input in the python tutor. This will help you identify the errors easily.
"""

#answer

main_dish = input()
time_of_day = int(input())
has_voucher = input()
is_card_payment = input()

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit()

if 12 <= time_of_day <=15:
    total_cost = (1 - 0.15) * cost
else:
    total_cost = cost

if has_voucher == 'True':
    total_cost = total_cost * 0.9  # Apply voucher discount

if is_card_payment == 'True': # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.02f}")