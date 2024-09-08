def mcarty(n):
    if (n > 100):
        return n - 10
    return mcarty(mcarty(n+11))

def main():
    n = int(input("mc carthy of:"))

    ans_rec = mcarty(n)
    print(ans_rec)


if __name__ == "__main__":
    main()