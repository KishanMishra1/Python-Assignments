'''Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.

The length of the list can be less than 4 also.'''

#lex_auth_0127135811649044481146
def find_nine(nums):
    if len(nums)>=4:
        for i in range(0,4):
            if nums[i]==9:
                return True
        return False
    else:
        for i in nums:
            if i==9:
                return True
        return False

nums = [1, 2, 9]
print(find_nine(nums))
