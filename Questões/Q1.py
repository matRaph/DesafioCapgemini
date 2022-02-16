
n = int(input())
aster = 1
for x in range(n):
    print(" " * (n - x) + "*" * aster)
    aster = aster + 1