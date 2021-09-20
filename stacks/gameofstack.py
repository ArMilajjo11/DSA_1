'''def twoStacks(maxSum, s1, s2):
    summ = 0
    count = 0
    s1.reverse()
    s2.reverse()
    while summ <= maxSum:
        if s1[0] > s2[0]:
            num = s2.pop()
        else:
            num = s1.pop()
        summ = summ + num
        if summ > maxSum:
            break
        count = count + 1
    return count'''

def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    stack = []
    total, score = 0, 0

    while a:
        item = a.pop()
        if (total + item) <= x:
            total += item
            score += 1
            stack.append(item)
        else:
            break

    maxScore = score

    while b:
        item = b.pop()
        total += item
        score += 1
        while total > x and stack:
            total -= stack.pop()
            score -= 1
        if total <= x and score > maxScore: maxScore = score

    return maxScore

g = int(input())
for i in range(g):
    l1, l2, maxSum = map(int, input().split())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    print(twoStacks(maxSum, s1, s2))