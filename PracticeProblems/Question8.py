'''Write a python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.

Suppose the following input is supplied to the function 
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.'''

# lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    # start writing your code here
    dep=0
    wid=0
    for i in trans_list:
        act,rs=i.split(":")
        if act=="D":
            dep+=int(rs)
        elif act=="W":
            wid+=int(rs)
    return dep-wid


trans_list = ["D:300", "D:200", "W:200", "D:100"]
print(calculate_net_amount(trans_list))
