'''Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants'''
def removev(word):
    w=list(word)
    v = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in word :
        if i in v:
            w.remove(i)
        else:
            pass
    return "".join(w)

def sms_encoding(data):
    data_l=data.split()
    v=['a','i','e','o','u','A','E','I','O','U']
    res=[]
    for i in data_l:
        if i not in v:
            res.append(removev(i))
        else:
            res.append(i)
    return " ".join(res)


    #start writing your code her
data="I love Python"
print(sms_encoding(data))
