
def steps(n):
    star = 1
    for x in range(n):
        print(" " * (n - x) + "*" * star)
        star = star + 1

steps(int(input()))