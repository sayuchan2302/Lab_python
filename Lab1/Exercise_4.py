def find_fibonacci (n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    a,b = 0,1
    for i in range (2 , n+1):
        a,b = b,a+b
    return b

print(find_fibonacci(10))