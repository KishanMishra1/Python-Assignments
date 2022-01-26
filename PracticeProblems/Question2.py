'''Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.

The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input: )()((()())

Expected Output : False'''



def bracket_pattern(input_str):
    start=0
    end=0
    if input_str.startswith('(') and input_str.endswith(')'):
        for i in input_str:
            if i=='(':
                start+=1
            else:
                end+=1
        if start==end and start+end==len(input_str):
            return True
    return False




input_str = "(())("
print(bracket_pattern(input_str))
