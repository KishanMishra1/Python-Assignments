
'''A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.

Write a python program to implement the following functions:

1. find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.

2. generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1,
how many have scored 3….how many have scored 25. The result should be populated in a list and returned.

3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.'''


#lex_auth_01269438947391897654

#Global variable
from typing import List

list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    global list_of_marks
    sum=0
    avg=0
    count=0
    count_avg=0
    for i in list_of_marks:
        sum+=i
        count+=1
    avg=sum/count
    for i in list_of_marks:
        if i>avg:
            count_avg+=1
    return (count_avg/count)*100


def sort_marks():
    a=list(list_of_marks)
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


def generate_frequency():
    freq = []
    global list_of_marks
    for x in range(26):
        count = 0
        for y in list_of_marks:
            if x == y:
                count += 1
        freq.append(count)
    return freq

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
