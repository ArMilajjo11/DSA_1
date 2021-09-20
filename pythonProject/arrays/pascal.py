# def generate(numRows):
#     lst = []
#     for i in range(0, numRows):
#         a = list(str(11**i))
#         lst.append(a)
#     return lst
# works only till n = 5
# n = 5
# print(generate(n))

def pascal(n):
    lst = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(lst[i-1][j-1]+lst[i-1][j])
        lst.append(temp)
    return lst

n = 6

# [[1],[1,1],[1,2,1],[1,3,3,1]]
print(pascal(n))