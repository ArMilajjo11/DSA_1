n, r = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n-r):
    a = arr[n-1]
    for j in range(n):
        arr[n-1-j] = arr[n-2-j]
    arr[0] = a
for k in arr:
    print(k, end=" ")

