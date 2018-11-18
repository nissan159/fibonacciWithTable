#by: Nissan Malko
#This function takes two paramaters
#N, being the posiiton in the fibonacci sequence that you want.
# Arr being an array that holds previously solved values

def recur_fib(n, arr):
    if len(arr) < 2:
        arr.append(0)
        arr.append(1)
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

#simple check
print(recur_fib(4, fibValue))