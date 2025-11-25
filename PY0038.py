def suma1(*args: float) -> float:
    total = 0
    for i in range(1, len(args) - 1):
        total += args[i]
    return total

def suma2(primero: float, *medio: float, ultimo: float) -> float:
    total = 0
    for num in medio:
        total += num
    return total

def suma3(*args: float) -> float:
    total = 0
    for num in args[1:-1]:
        total += num
    return total

print(suma1(1,2,3,4,5,))
print(suma2(1,2,3,4, ultimo=5))
print(suma1(1,2,3,4,5,))
