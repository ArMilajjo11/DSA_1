from math import ceil
# def majorityElement(lst):
#     lst = sorted(lst)
#     n = ceil(len(lst)/2)
#     count = 1
#     for i in range(len(lst)-1):
#         if lst[i] == lst[i+1]:
#             count += 1
#             if count == n:
#                 return lst[i]
#             else:
#                 continue
#         else:
#             count = 1
#     return lst[0]

# def majorityElement(lst):
#     lst = sorted(lst)
#     l = len(lst)
#     n = ceil(l/2)
#     if l <= 1:
#         return lst[0]
#     else:
#         return lst[n]
#
# def majorityElement(lst):
#     dict = {}
#     for i in lst:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] = dict[i] + 1
#     k = list(dict.keys())
#     v = list(dict.values())
#     return k[v.index(max(v))]

def majorityElement(lst)
    
lst = [3,3,4]
print(majorityElement(lst))

