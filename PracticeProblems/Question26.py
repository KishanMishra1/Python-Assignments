# lex_auth_0127136253311385601197

def check_occurence(string):
    string=string.lower()
    if string.count("mat")==string.count("jet"):
        return True
    else:
        return False


# start writing your code here

string = "Jet on the Mat but mat is too long"
print(check_occurence(string))
