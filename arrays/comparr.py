n = int(input())
strings, queries = list(), list()
for i in range(n):
    strings.append(input())
q = int(input())
for j in range(q):
    queries.append(input())
for k in queries:
    count = 0
    for l in strings:
        if k == l:
            count = count + 1
        else:
            continue
    print(count)
    





