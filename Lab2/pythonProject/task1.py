def task1 () :
    n = int(input("insert n: "))
    L = []
    for i in range(1 , n+1) :
        number = int(input(f"insert number {i}: "))
        L.append(number)
    #print min & max
    print("Max element in L: " ,max(L))
    print("Min element in L: " , min(L))

    #sum list
    total = 0
    for e in L :
        total += e
    print ("Sum of elements in L: " , total)

    #sort asc element in L
    print("Sorted L asc: ", sorted(L))
    #count positive & nagative
    positiveCount = 0
    negativeCount = 0
    for e in L :
        if e < 0 :
            negativeCount += 1
        elif e > 0 :
            positiveCount += 1
    print ("Positive elements in L: " , positiveCount)
    print ("Negative elements in L: " , negativeCount)

task1()