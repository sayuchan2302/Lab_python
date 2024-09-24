def func1 (n) :
    result = 0
    for i in range(1,n+1):
        if i%2 ==0 :
            result -= i
        else :
            result += i
    return result

def factorial (n) :
    if n == 0 or n ==1 :
        return 1
    return n * factorial(n-1)

def func2 (n) :
    result = 0
    for i in range (1 , n + 1) :
        result += factorial(i)
    return result

def func3 (n) :
    result = 0
    for i in range (1, n + 1) :
        result += i **2
    return result
def factorialOfEvens(n) :
    product = 1
    for i in range(1,n + 1) :
        product *= 2 * i
    return product

def func4 (n) :
    result = 0
    for i in range (1, n + 1) :
        if i == 0 :
            result += 1
        else :
            result += factorial(i)
    return result
    #example
print(func1(7))
print (func2(3))
print(func3(3))
print(func4(7))


