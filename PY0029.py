def fibo(n:int) -> list[int]:

    n1 = 0
    n2 = 1
    fibo = [n1, n2]
    for _ in range(2, n):
        n2 = n1 + n2
        n1 = n2 - n1
        fibo.append(n2)
    return fibo

print(fibo(10))