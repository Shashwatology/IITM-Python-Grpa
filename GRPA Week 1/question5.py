'''
Question 
GrPA 5 - (Input Output and Type conversion) - GRADED
Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")
Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.
Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".
Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.
'''

#Answer 
age = int(input())
dob = input().strip()   # format: dd/mm/yy

day, month, year = map(int, dob.split('/'))

# Fifth birthday
fifth_birthday = f"{day}/{month}/{year + 5}"

# Last birthday
last_birthday = f"{day}/{month}/{year + age}"

# Same day after 10 months
new_month = month + 10
new_year = year

if new_month > 12:
    new_month -= 12
    new_year += 1

tenth_month = f"{day}/{new_month}/{new_year}"

print(f"{tenth_month}, {fifth_birthday}, {last_birthday}")

weight = float(input())

kg = int(weight)
grams = int(round((weight - kg) * 1000))

weight_readable = f"{kg} kg {grams} grams"

print(weight_readable)
