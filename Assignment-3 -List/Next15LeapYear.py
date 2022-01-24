def isleap(year):
    if year%400==0 and year%100==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False


def find_leap_years(given_year):
    list_of_leap_years=[]
    while(len(list_of_leap_years)!=15):
        if isleap(given_year):
            list_of_leap_years.append(given_year)
        else:
            pass
        given_year+=1
    return list_of_leap_years

list_of_leap_years=find_leap_years(1684)
print(list_of_leap_years)
