arr, add = list(), list()
for i in range(6):
    arr.append(list(map(int, input().split())))
for j in range(len(arr)-2):
    for k in range(len(arr)-2):
        add.append(arr[j][k] + arr[j][k + 1] + arr[j][k + 2] + arr[j + 1][k + 1] + arr[j + 2][k] + arr[j + 2][k + 1] +
                   arr[j + 2][k + 2])
print(max(add))




