lst = [0, 1, 0, 3, 12]
l = len(lst)
j = 0
for i in range(l):
    if lst[i] != 0:
        lst[j] = lst[i]
        j += 1
for k in range(l-j):
    lst[j+k] = 0
print(lst)




