

# Take the input from standard input using input()
# and print the output according to the problem .

# Write your code here

num = int(input())
for i in range(num):
    sentence = input()
    sentence = sentence.split(",")
    max = 0
    count = 1
    for seq in range(1,len(sentence)):
        if sentence[seq-1][-1] == sentence[seq][0]:
            count = count + 1 
        else: 
            if max < count: 
                max = count
            count = 1
        
    if max<count:
        max = count
    print(max) 
