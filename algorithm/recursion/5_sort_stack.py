def sorted(s):
    # Code here
    if(len(s) == 0):
        return
    temp = s.pop()
    sorted(s)
    Insert(s, temp)


def Insert(s, temp):
    if(len(s) == 0 or s[-1] >= temp):
        s.append(temp)
        return
    val = s.pop()
    Insert(s, temp)
    s.append(val)
    return
