'''
GrPA 3 - Nested loops - GRADED
Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:
Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
'''

#Answer
task = input()

if task == 'permutation':
    s = input()
    for i in s:
        for j in s:
            if (i != j):
                print(f'{i}{j}')

elif task == 'sorted_permutation':
    s = input()
    for i in s:
        for j in s:
            if ((i != j) and (i < j)):
                print(f'{i}{j}')

elif task == 'repeat_the_repeat':
    n = int(input())
    for i in range(1, n + 1):
        repeat_the_repeat = 0
        for j in range(1, n + 1):
            repeat_the_repeat = (repeat_the_repeat * 10) + j
        print(repeat_the_repeat)

elif task == 'repeat_incrementally':
    n = int(input())
    if (n > 0):
        repeat_incrementally = 0
        for i in range(1, n + 1):
            repeat_incrementally = (repeat_incrementally * 10) + i
            print(repeat_incrementally)

elif task == 'increment_and_decrement':
    n = int(input())
    if (n > 0):
        increment = ''
        for i in range(1, n + 1):
            increment = increment + str(i)
            decrement = increment[-2::-1]
            increment_and_decrement = increment + decrement
            print(increment_and_decrement) 
