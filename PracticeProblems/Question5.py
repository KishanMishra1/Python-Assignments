'''Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.'''

# lex_auth_0127135838317445121147
def retlist(word):
    counta=0
    countn=0
    for i in word:
        if i.isalpha():
            counta += 1
        else:
            countn += 1
    return [counta, countn]



def count_digits_letters(sentence):
    sen=sentence.replace(";","").replace("-","").replace("."," ")
    sen=sen.split(" ")
    print(sen)
    sumx=[]
    suma=0
    sumd=0
    if len(sen)==1:
        return retlist(sen[0])
    elif len(sen)>1:
        for i in sen:
            sumx.append(retlist(i))
        for i in sumx:
            suma+=i[0]
            sumd+=i[1]
        return [suma,sumd]







sentence = "Come to Block-1"
print(count_digits_letters(sentence))
