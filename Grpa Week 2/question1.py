''' GrPA 1 - Variables and Assignment - GRADED
Solve all the below tasks related to variables.
This exercise gives you practice in working with variables.
Note: Do not take input or print output as they are taken care by the suffix code(evaluator).
'''

#answer - 

x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

x1, x2 = x2, x1 # swap the values of `x1` and `x2`

y1, y2, y3 = y2, y3, y1 # do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 

a = z # create a new variable `a` with the value of `z`

del z  # delete the variable `z`

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)