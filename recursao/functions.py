import math

def f10(a, b):
    if (b == 0):
        return 0
    
    if (b % 2 == 0):
        return f10(a + a, math.floor(b / 2))
    else:
        return f10(a + a, math.floor(b / 2)) + a

def f11(a, b):
        
    print(f"a: {a}, b: {b}")
    print(f"{a} * {a} = {a*a}")
    print(f"floor({b} / 2 = {math.floor(b / 2)}\n")
    
    if (b == 0):
        return 1
    
    if (b % 2 == 0):
        return f11(a * a, math.floor(b / 2))
    else:
        return f11(a * a, math.floor(b / 2)) * a


def main():
    a, b = map(int, input("function (a, b): ").split())
    
    ans_f10 = f10(a, b)
    ans_f11 = f11(a, b)

    print(ans_f10, ans_f11)


if __name__ == "__main__":
    main()