def mdc(a, b):
    if (b == 0):
        return a
    
    return mdc(b, a % b)

def mdc_iter(a, b):
    remainder = 1
    while remainder > 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def main():
    a, b = map(int, input("mdc (a, b): ").split())
    
    ans_rec = mdc(a, b)
    ans_iter = mdc_iter(a, b)

    print(ans_rec, ans_iter)


if __name__ == "__main__":
    main()