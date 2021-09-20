def squareroot(x):
    low = 1
    high = x
    while low <= high:
        mid = (high+low)//2
        if mid*mid == x:
            return mid
        if mid*mid < x:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans


x = int(input("Enter number: "))
print(squareroot(x))

# def binarysearch(arr, x):
#     l = len(arr)
#     low = 0
#     high = l-1
#     mid = 0
#     while low <= high:
#         mid = (high+low)//2
#         if x < arr[mid]:
#             high = mid - 1
#         elif x > arr[mid]:
#             low = mid + 1
#         else:
#             return mid
#     return "gaand marao"
#
# arr = [2, 3, 4, 10, 40]
# x = 40
# print(binarysearch(arr,x))
#
#
