'''Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.'''

# lex_auth_0127135869481369601150

def list123(nums):
    num=""
    for i in nums:
        num+=str(i)
    if "123" in num:
        return True
    return False

# start writing your code here


nums = [1, 2, 1, 2, 1]
print(list123(nums))
