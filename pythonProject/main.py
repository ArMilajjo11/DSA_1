def findDuplicate(lst):
    lst = sorted(lst)
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            n = lst[i]
            return n
        else:
            continue
    if n == lst[-1]:
        return n




# 1 2 3 3 4
lst = [3,1,3,4,2]
print(findDuplicate(lst))