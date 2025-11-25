def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fib = fibonacci()

    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
