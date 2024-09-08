def fatorial(n):
    if (n == 0):
        return 1
    return n * fatorial(n-1)

def fatorial_iter(n):
    answer = 1
    i = 2

    while (i <= n):
        answer *= i
        i += 1
    return answer

def main():
    n = int(input("fatorial of: "))
    ans_rec = fatorial(n)
    ans_iter = fatorial_iter(n)

    print(ans_rec, ans_iter)
    
    
if __name__ == "__main__":
    main()