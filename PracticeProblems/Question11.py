'''Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.'''

def find_upper_and_lower(sentence):
    up,low=0,0
    for i in sentence:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1
        else:
            pass


    return [up,low]
