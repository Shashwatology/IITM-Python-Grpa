

def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    final = []
    for i in student_courses.values():
        final.append(i)
    semifinal = []  
    for i in final:
        for j in i:
            semifinal.append(j)
    dic = {}
    for i in semifinal:
        dic[i] = dic.get(i,0) + 1
        
    final_final_final = [] 
    for i in sorted(dic.values())[::-1]:
        for k,j in zip(dic.keys(),dic.values()):
            if i == j:
                final_final_final.append(k)
                
    return final_final_final
