def taxi_fare (d , t) :
    if d <= 0 or t <= 0 :
        return 0
    fare = 0
    if d > 0 :
        fare += 10000
        if d > 1 :
            if d <= 10 :
                fare += (d-1)*5000
            else :
                fare += 9 *5000
                fare += (d -10) * 2
    fare += t*1000
    return fare

## example
print(taxi_fare(20 , 7) , "VND")
