
def palindrome(word,i,j):
    if i==j:
        return True
    if word[i]!=word[j]:
        return False
    if i<j+1:
        return palindrome(word,i+1,j-1)
    return True

def is_palindrome(word):
    word=word.lower()

    if len(word)==0:
        return True
    else:
        return palindrome(word,0,len(word)-1)

    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("katak")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
