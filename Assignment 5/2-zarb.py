def jadval_zarb(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(f"{i * j:4}", end="")
        print()

n = int(input("please enter row  : "))
m = int(input("please enter column : "))

jadval_zarb(n, m)