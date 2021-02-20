import random
a = int(input("введите число"))
def gen(n):
    n = 0
    pr = []
    while (n!=a):
        num = random.randrange(100)
        n += 1
        if num in pr:
            num = 100+n
        b = [random.randrange(100) for i in range(0, num)]
        pr.append(num)

        if n % 2 == 0:
            b.sort()
        else:
            b.sort(reverse=True)
        print(b)
gen(a)
