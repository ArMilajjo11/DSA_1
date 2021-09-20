n = int(input("Enter number of monster: "))
inexp = int(input("Enter initial exp: "))
monsters = dict()
temp = list()
for i in range(n):
    temp.append(int(input("Enter power of monster "+str(i+1)+" ")))
for j in range(n):
    b = int(input("Enter bonus of monster "+str(j+1)+" "))
    monsters[temp[j]] = b

temp = sorted(temp)
print(temp)
count = 0
for k in temp:
    if inexp >= k:
        inexp += monsters[k]
        print("inexp: ",inexp)
        count += 1
    else:
        break
print("Monsters defeated ",count)






