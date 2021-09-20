def prime(n):
    lst = [i for i in range(n)]
    main = [True for i in range(n)]
    p = 2
    for j in range(p+1,n):
        print("This is",p)
        if lst[j] % p == 0:
            main[j] = False
        else:
            continue
        p += 1
    return lst,main

n = int(input("Enter no. "))
print(prime(n))
