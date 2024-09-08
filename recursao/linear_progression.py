def lp(a, r, n):
    if (n == 1):
        return a
    return lp(a, r, n - 1) + r

def lp_iter(a, r, n):
    return a + (n - 1) * r



def main():
    a, r, n = map(int, input("calculate linear progression general term (a, r, n): ").split())
    
    ans_rec = lp(a, r, n)
    ans_iter = lp_iter(a, r, n)

    print(f"rec {ans_rec}")
    print(f"iter {ans_iter}")
    

if __name__ == "__main__":
    main()