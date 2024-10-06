def task3 (lst : list) -> bool:
    asc = True
    desc = True
    previous = lst[0]
    for e in lst[1:] :
        if e >  previous :
            asc = False
            previous = e
        if e < previous :
            desc = False
            previous = e
        if asc != True and desc != True :
            return False
    return True
L1 = [3,1,4,5,6]
L2 = [6,7,8,9,11]
L3 = [8,4,1,0]

print (task3(L3))