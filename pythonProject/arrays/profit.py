def maxProfit(lst):
    profit = 0
    min = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < min:
            min = lst[i]
        profit = max(profit, lst[i] - min)
    return profit


n = [7,1,5,3,6,4]
print(maxProfit(n))

# def maxProfit(lst):
#     l = len(lst)
#     profit = 0
#     for i in range(l):
#         for j in range(i+1,l):
#             if lst[i] > lst[j]:
#                 continue
#             elif lst[i] < lst[j]:
#                 a = lst[j] - lst[i]
#                 if a > profit:
#                     profit = a
#                 else:
#                     continue
#     return profit