def plusOne(digits):
    digits = list(map(str, digits))
    num = "".join(digits)
    num = int(num) + 1
    return list(str(num))

digits = list(map(int, input().split()))
x = plusOne(digits)
print(x)