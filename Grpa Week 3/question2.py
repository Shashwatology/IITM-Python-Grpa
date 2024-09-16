'''
GrPA 2 - For Loop - GRADED
Bit of Wisdom 📖 In context of general incremental definite loops the structure of while loop can be converted to a for loop using range. Refer this.
# the wile loop
i = 0 # initialization
while i<10: # condition
    print(i) # body
    i+=2 # update
# same with for loop
for i in range(0,10,2): # range combines initalization, temination and update.
    print(i)
'''

#answer 

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    for i in range (1 , n+1):
       result *= i

    print(result)


elif task == 'even_numbers':
    n = int(input())
    for i in range (0 , n +1 , 2):
        print(i)

elif task == 'power_sequence':
    n = int(input())
    result = 1
    for i in range(n):
        print(2**i)


elif task == 'sum_not_divisible':
    n = int(input())
    sum = 0
    for i in range(1 , n):
        if (i % 4 != 0 and i % 5 != 0 ):
            sum += i
    print(sum)

elif task == 'from_k':
    n = int(input())
    k = int(input())
    count = 0
    for i in range (k,0,-1):
        str_i = str(i)
        if "5" not in str_i and '9' not in str_i and i%2!=0 :
            print(str_i[::-1])
            count += 1
            if count == n :
                break

elif task == 'string_iter':
    n = input()
    prev = 1
    for i in range(len(n)):
        curr = int(n[i])
        print(curr * prev)
        prev = curr

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for i in lst:
        print(f'{i} - type: {type(i)}')

else:
    print("Invalid")