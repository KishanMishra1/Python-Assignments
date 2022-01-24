'''Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.'''

"'USELESS TESTCASE 2..NOT PASSED"'
import sys

def max_frequency_word_counter(data):
    data_l=data.split()
    dict={}
    frequency=0
    count=0
    for i in data_l:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    max=-sys.maxsize-1
    for j in dict.values():
        if j>max:
            max=j
    for i, j in dict.items():
        if j == max:
            p=i
    print("{} {}".format(p, max))




#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
