def task4(arr):
    n = len(arr)
    result = arr[:]
    for i in range(n):
        if arr[i] == -1:
            left_neighbor = None
            right_neighbor = None
            for j in range(i - 1, -1, -1):
                if arr[j] != -1:
                    left_neighbor = arr[j]
                    break
            for j in range(i + 1, n):
                if arr[j] != -1:
                    right_neighbor = arr[j]
                    break
            if left_neighbor is not None and right_neighbor is not None:
                result[i] = (left_neighbor + right_neighbor) // 2

    return result

# Test case
arr = [10, 11, 12, -1, 14, 16, 17, 19, 20]
resultArr = task4(arr)
print(resultArr)
