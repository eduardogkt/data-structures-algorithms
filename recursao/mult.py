def mult(n, m):
    if (n == 0):
        return 0
    
    if (n < 0):
        return -m + mult(n + 1, m)
    elif (n > 0):
        return m + mult(n - 1, m)

def mult_iter(n, m):
    if (n == 0 or m == 0):
        return 0
    
    answer = 0
    i = 0
    if (n < 0):
        while i > n:
            answer -= m
            i -= 1
    else:
        while i < n:
            answer += m
            i += 1
    
    return answer

def main():
    print("multiply n * m: ")
    n = int(input("n: "))
    m = int(input("m: "))
    

    ans_rec = mult(n, m)
    ans_iter = mult_iter(n, m)

    print(ans_rec, ans_iter)


if __name__ == "__main__":
    main()