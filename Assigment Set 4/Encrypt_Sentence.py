'''Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change'''
def even(word):
    return "".join(str(a) for a in word[::-1])

def odd(word):
    vow2=[]
    cons=[]
    vow=['a','i','e','o','u']
    for i in word :
        if i in vow:
            vow2.append(i)
        else:
            cons.append(i)
    return "".join(cons+vow2)


def encrypt_sentence(sentence):
    k=sentence.split(" ")
    k1=[]
    for i in range(len(k)):

        if i%2==0:
            k1.append(even(k[i]))
        else:
            k1.append(odd(k[i]))
    return " ".join(str(a) for a in k1)


sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)

