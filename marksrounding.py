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

def gradingStudents(grades):
    for i in range(0,len(grades)):
        if grades[i]>=38:
            for j in range(grades[i],101):
                l1=[]
                if j%5==0:
                    l1.append(j)
                    if l1[0]-grades[i]<3:
                        grades[i]=l1[0]
    return(grades)
if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
