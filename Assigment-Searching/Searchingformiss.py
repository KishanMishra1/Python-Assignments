#lex_auth_0127667326864670723497

def find_unknown_words(text,vocabulary):
    res=set()
    text=text.lower()
    text=text.replace(".","").replace("?","").replace("!","")
    text=text.split()
    for i in text:
        if i not in vocabulary:
            res.add(i)
        else:
            pass
    if len(res)>0:
        return res
    else:
        return -1

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
