'''
GrPA 2 - Formatting Outputs - GRADED
Implement the below functions where you have to format the given data in the given format and print them to the standard output according to the docstring given.
'''

#answer

import random

def display_student_details(name:str, age:int, rollno:int):
    '''
    Given name, age, and rollno of student,
    print them over multiple lines
    Output format:
    name
    age
    rollno
    Return: None
    '''
    print(name)
    print(age)
    print(rollno)

# heterogeneous values - single line
def display_student_details_same_line(name:str, age:int, rollno:int):
    '''
    Given name, age, and rollno of student,
    print them in the same line separated by a comma.
    Output format:
    name,age,rollno
    '''
    print(name,age,rollno,sep=",")

# homogeneous - single line
def display_comma_separated_integers(nums:list):
    '''
    Given a list of nums print them in the same line 
    separated by commas.
    For example, if  nums= [1,3,4,5],
    Output format:
    1,3,4,5
    '''
    print(*nums, sep=",")

# homogeneous - multi-line - definite
def display_float_nums_over_multiple_lines(nums:list):
    '''
    Given a list of floating point nums print them 
    over multiple lines with 3 digits after the decimal point.
    For example, if nums = [1.2, 3.4,5.6,7.8]
    Output format:
    1.200
    3.400
    5.600
    7.800
    '''
    for num in nums:
        print(f"{num:.3f}")

# homogeneous - indefinite
def display_random_ints(seed:int):
    '''
    Given a random seed, set the random seed and 
    generate multiple random integers within the range [0,100] 
    (using `randint(0,100)`), until 0 is encountered and 
    print it with max 10 comma seperated ints per line over multiple lines
    Output format
    34,26,73,82,35,36,7,4,27,46
    6,33,62,78,0
    '''

    random.seed(seed)
    count = 0
    nums = []
    while True:
        num = random.randint(0,100)
        nums.append(num)
        if num == 0:
            break
        count +=1
        if count % 10 == 0:
            print(*nums, sep=",")
            nums = []
    print(*nums, sep=",")

# hybrid - single line
def display_batsman_runs(name:str, number:int, runs:list):
    '''
    Given name, number and runs scored by a batsman
    display the name, number and runs separated by commas in the same line.
    For example, if name="player1", number=9 and runs=[2,3,4,4,6]
    Output Format;
    player1,9,2,3,4,4,6
    '''
    print(name,number,*runs,sep=",")

# key value
def display_course_scores(course_scores:dict):
    '''
    Given a dictionary of course scores with 
    course name as keys and course scores as values. 
    Format each course score pair separated by colon(':') 
    on each line where each pair is printed over multiple lines 
    in the ascending order of keys.
    For example, if course_scores = {"course1":78, "course3":89,"course2":90}
    Output format:
    course1:78
    course2:90
    course3:89
    '''
    for key in sorted(course_scores):
        print(f"{key}:{course_scores[key]}")

def display_all_batsman_runs(batsman_runs:list):
    '''
    Given a list of tuple of batsman runs, 
    print the batsman name and comma separated runs
    which are separated by a hyphen and printed over multiple lines.
    Arguments: batsman_runs: list[tuple(str, list[int])]
    For example, if batsman_runs = [
        ("batsman1",[1,2,1,4,6,2,2,1]),
        ("batsman2",[2,2,6,4,1]),
        ("batsman3",[6,1,2,4,4,2])
    ]
    Output format:
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2
    '''
    for batsman in batsman_runs:
        print(f"{batsman[0]}-{','.join(str(x) for x in batsman[1])}")

def display_student_marks(student_marks:list):
    '''
    Given the student rollno, city, age and marks of 
    course1, course2 and course3 as a list of dicts,
    print the attributes of each student in a single 
    line as comma separated values (in the previously mentioned order) 
    and print the whole list over multiple lines.
    Arguments: student_marks: list[dict] where the keys of the dict are 'rollno':int,'city':str, 'age':int, 'course1':int, 'course2':int,'course2':int
    For example, if student_marks = [
        {'rollno': 1, 'city': 'chennai', 'age': 23, 'course1': 86, 'course2': 69, 'course3': 86}, 
        {'rollno': 2, 'city': 'mumbai', 'age': 19, 'course1': 78, 'course2': 65, 'course3': 89}
    ]
    Output: 
    1,chennai,23,86,69,86
    2,mumbai,19,78,65,89
    '''
    for student in student_marks:
        print(f"{student['rollno']},{student['city']},{student['age']},{student['course1']},{student['course2']},{student['course3']}")

def display_student_marks_over_multiple_lines(student_marks:list):
    '''
    Same input as the above function, but print each attribute 
    over mulitple line in the same order of attributes as the previous one.
    For the example given in the above input,
    Output:
    1
    chennai
    23
    86
    69
    86
    2
    mumbai
    19
    78
    65
    89
    '''

    for student in student_marks:
        print(student['rollno'])
        print(student['city'])
        print(student['age'])
        print(student['course1'])
        print(student['course2'])
        print(student['course3'])

# this basically reads the input and executes it as code
import sys
exec(sys.stdin.read())