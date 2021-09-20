def singleNumber(lst):
    lst = sorted(lst)
    num = 0
    for i in range(0,len(lst)-1,2):
        if lst[i] == lst[i+1]:
            continue                 # SO SEXYYYYYYYYYUIDHFEWUGEWUFGSEJYFGY
        else:
            num = lst[i]
            return num
    if num != lst[-1]:
        return lst[-1]



lst =  [1]
print(singleNumber(lst))