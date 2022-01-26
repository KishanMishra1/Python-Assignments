'''Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. 
The length of the strings should be the same.'''







#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    #start writing your code here
    data1=data1.lower()
    data2=data2.lower()
    if len(data1)!=len(data2):
        return False
    if sorted(data1)!=sorted(data2):
        return False
    k=len(data1)
    res=0
    s=0
    c=0
    for i in range(0,len(data1)-1):
        if data1[i]!=data2[i] :
            res+=1
        else:
            s+=1
    if s>0:
        return False
    return True

if __name__ == '__main__':
    print(check_anagram("Schoolmaster","Theclassroom"))
