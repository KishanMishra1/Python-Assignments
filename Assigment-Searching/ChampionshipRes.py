#lex_auth_0127667391112806403379

def find_matches(country_name):
    res=[]
    for i in match_list:
        cn,cham,m,w=i.split(":")
        if cn==country_name:
            res.append(i)
    return res
def max_wins():
    pass

def find_winner(country1,country2):
    c1=0
    c2=0
    for i in match_list:
        cn,cham,m,w=i.split(":")
        if cn==country1:
            c1+=int(w)
        elif cn==country2:
            c2+=int(w)
    if c1>c2:
        return country1
    elif c1==c2:
        print("TIE")
    else:
        return country2



#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(find_winner('AUS','IND'))
print(find_matches('AUS'))
