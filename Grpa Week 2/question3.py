'''
Question 
GrPA 3 - Basic conditional patterns - GRADED
This problem gives you exposure to different use cases of if ... elif and else conditional structues.
Part 1 - Only if
Part 2 - if ... else
Part 3 - if ... elif
'''

#Answer 

# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from new_word if it is there
if new_word.endswith("ing"):
    new_word = new_word[:-3]

# add the suffix "ing" to new_word if continuous_tense is True
if continuous_tense:
    new_word += "ing"
# write the whole if else block here

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age >= 18:
    age_group = "Adult"
else:
    age_group = "Child"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
if is_member:
    applicant_type = age_group + " Member"
else:
    applicant_type = age_group + " Non-member"
# write the whole if else block

# part 3 if ... elif .. else

# based on the value of color_code assign the color value in lower case and "black" if color_code is none of R, B and G

if color_code == "R":
    color = "red"
elif color_code == "G":
        color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

hrs = int(time[:2])
is_time_valid = 0 < hrs <= 12 # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
am_pm = time[-2 : ]
if am_pm == "AM":
    if hrs == 12:
        time_in_hrs = 0
    else:
        time_in_hrs = hrs
else:
    if hrs == 12:
        time_in_hrs = 12
    else:
        time_in_hrs = hrs + 12

#time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range
if (is_time_valid):
    if 6 <= time_in_hrs < 12:
        time_of_day = "Morning"
    elif 12 <= time_in_hrs < 18:
        time_of_day = "Afternoon"
    elif 18 <= time_in_hrs <= 23:
        time_of_day = "Evening"
    elif 0 <= time_in_hrs <= 6:
        time_of_day = "Night"
else:
    time_of_day = "Invalid"


# write your code here