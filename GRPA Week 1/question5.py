'''
Question 
GrPA 5 - (Input Output and Type conversion) - GRADED
Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")
Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.
Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".
Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.
'''

#Answer 

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
# <eoi>

output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[:3] # str: get the first 3 characters of s

output4 = s[::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1]  # str: get the reverse of s

course_term = int(course_code[3]) # int: get the term of the year as number from course_code
course_year = int(course_code[0 :2]) # int: get the year as two digit number from course_code