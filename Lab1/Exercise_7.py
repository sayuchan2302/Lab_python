def draw_pyramid(n) :
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ", end ="")
        for x in range (1 ,2*i -1 +1) :
            print("X", end= "")
        print()


## test
draw_pyramid(5)