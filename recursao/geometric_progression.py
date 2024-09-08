def gp(a, r, n):
    if (n == 1):
        return a

    return (a * (r ** (n-1))) + gp(a, r, n-1)


def gp_iter(a, r, n):
    return ( a * ((r ** n) - 1) ) / (r - 1)


def main():
    a, r, n = map(int, input("calculate geometric progression sum (a, r, n): ").split())
    
    ans_rec = gp(a, r, n)
    ans_iter = gp_iter(a, r, n)

    print(f"rec {ans_rec}")
    print(f"iter {ans_iter}")
    

if __name__ == "__main__":
    main()