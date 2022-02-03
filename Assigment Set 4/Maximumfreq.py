'''Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.'''


#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    dict2={}
    data=data.lower()
    data_l=data.split(" ")
    for i in data_l:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i]=1
    max_freq=max(dict2.values())
    #print(max_freq)
    max_freq_words=[]
    for i in dict2:
        if dict2[i]==max_freq:
            max_freq_words.append(i)
    #print(max_freq_words)
    if len(max_freq_words)==1:
        print( max_freq_words[0]+" "+str(max_freq))
    else:
        max_le=0
        max_word=""
        for i in max_freq_words:
            if len(i)>max_le:
                max_le=len(i)
                max_word=i
        print(max_word+" "+ str(max_freq))



#Provide different values for data and test your program.
data="Work like you do not need money love like you have never been hurt and dance like no one is watching is is"
max_frequency_word_counter(data)
