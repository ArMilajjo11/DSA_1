def mergeSorted(num1, num2, m, n):
    num3 = num1 + num2
    num4 = sorted(num3)
    for i in range(n):
        num4.pop(0)
    for j in range(m):
        num1[j] = num4[j]


num1 = list(map(int, input().split()))
m = len(num1)
num2 = list(map(int, input().split()))
n = len(num2)
print(mergeSorted(num1,num2, m, n))
print(num1)