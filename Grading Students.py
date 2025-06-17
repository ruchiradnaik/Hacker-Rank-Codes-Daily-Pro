import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def round_off(grades_item):
    
        grade_diff = (5 - grades_item % 5)
        if(grades_item % 5 != 0 and grade_diff < 3):
           grades_item = grades_item + grade_diff
        return grades_item
        
def gradingStudents(grades):
    final_grade = []
    for grade in grades:
        if (grade < 38):
            final_grade.append(grade)
        else:
            final_grade.append(round_off(grade))
    return final_grade
    
if __name__ == "__main__":
    grade_count = int(input("Enter grade count: "))
    grades = []
    for _ in range(grade_count):
        grades_item = int(input("Enter grade: "))
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)