'''
Problem 4 - I/O Based Problem Solving - GRADED
Find the perimeter of a bar graph given the heights at each bar. Assume width of each bar is 1 unit and height is atleast 1 unit and the heights of each bar is given as integers.
Input format
First line will have the number of bar graphs, say n.
Next n lines will have space seperated values
Output format
Perimeter of each bar graph printed over multiple lines
Example
5 3 4 1 3 2 5
bar_graph
'''


#answer 

def cal_perimeter(hts):
  perimeter=2* len(hts)
  for i in range(len(hts)-1):
      perimeter+=abs(hts[i]-hts[i+1])
  return perimeter + hts[0]+hts[-1]

n=int(input())
for i in range(n):
    hts=list(map(int, input().split()))
    perimeter=cal_perimeter(hts)
    print(perimeter)