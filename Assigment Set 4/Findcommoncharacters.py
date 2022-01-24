'''Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.'''

def find_common_characters(msg1,msg2):
    str=""
    for i in msg1:
        if i in msg2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" ","")
    else:
        return -1

 #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
