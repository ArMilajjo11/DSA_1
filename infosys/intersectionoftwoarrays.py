def bitonic(arr):
    l = len(arr)
    max = 0
    high = 0
    for i in range(l):
        if arr[i+1]> arr[i]:
            max = arr[i+1]
            high = i+1
        elif arr[i+1]<arr[i]:
            return high
        else:
            return -1

arr = [5, 6, 7, 8, 9, 10, 3, 2, 1]
print(bitonic(arr))