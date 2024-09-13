'''
GrPA 5 - min, max, sorted, groupby - GRADED
Implement all the given functions below according to the docstring.'''

#amswer

import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]



from collections import Counter
def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    grouped_data = {}

    for item in data:
        group_key = key(item)
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)

    return grouped_data
    ...

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    return {key: func(items) for key, items in groups.items()}
    ...

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    # min_=float('inf')
    # for i, mark in student_data.items():
    #     min_=min(mark[course],min)
    # marks = [mark[course] for mark in student_data]
    return min(list(map(lambda x: x[course],student_data)))
    ...

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    return max(list(map(lambda x: x[course],student_data)))
    ...

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    max_mark = max_course_marks(student_data,course)
    list_max = list(map(lambda x: x[course],student_data))
    max_index = list_max.index(max_mark)
    roll = list(map(lambda x: x["rollno"],student_data))
    return roll[max_index]
    ...

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    return list(map(lambda student: student['rollno'], sorted(
        student_data, 
        key=lambda x: (x[course1], x[course2], x[course3], x['rollno'])
    )))
    ...

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    city_counter = Counter(student['city'] for student in student_data)
    return dict(city_counter)
    ...

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    city = count_students_by_cities(student_data)
    return max(city, key=city.get)
    ...

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    grouped_data = groupby(student_data, key=lambda x: x['city'])
    return {city: sorted([student['rollno'] for student in students]) for city, students in grouped_data.items()}
    ...

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    grouped_data = groupby(student_data, key=lambda x: x['city'])
    avg_marks_by_city = {
        city: sum(student[course] for student in students) / len(students)
        for city, students in grouped_data.items()
    }
    return max(avg_marks_by_city, key=avg_marks_by_city.get)