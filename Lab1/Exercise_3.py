def findMaxM (n) :
    m = 0
    totalSum = 0
    while totalSum +m +1 < n :
        m+=1
        totalSum += m
    return m

n = 19
m = findMaxM(n)
print ("The maximal integer m : ", m)