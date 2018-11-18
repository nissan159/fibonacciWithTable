def recur_fib(n, arr):
    if(n < len(arr)):
        return (arr[n])
    else:
        value1 = 0
        value2 = 0
        if(n - 1 < len(arr)):
            value1 = arr[n-1]
        else:
            value1 = recur_fib(n - 1, arr)
        if(n - 2 < len(arr)):
            value2 = arr[n-2]
        else:
            value2 = recur_fib(n - 2, arr)
        return (value1 + value2)



fibValue = []
fibValue.append(0)
fibValue.append(1)

print(recur_fib(9, fibValue))