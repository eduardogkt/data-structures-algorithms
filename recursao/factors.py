def factors(a):
    if a == 1:
        print(a)
        return
    factors(a-1)

def factors_iter(a):
    for i in range(1, a+1):
        if (a % i == 0):
            print(i)

def main():
    a = 16
    factors_iter(a)

if __name__ == "__main__":
    main()
                    