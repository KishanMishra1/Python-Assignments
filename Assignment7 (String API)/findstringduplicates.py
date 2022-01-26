def remove_duplicates(value):
    s=set(value)
    s="".join(s)
    t=""
    for i in value:
        if i in t:
            pass
        else:
            t=t+i
    return t
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
