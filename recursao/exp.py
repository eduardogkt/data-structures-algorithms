def exp_iter(x, n):
    if (n == 0):
        return 1
    
    answer = 1
    i = 0
    while (i < n):
        answer *= x
        i += 1
    
    return answer

def exp(x, n):
    if (n == 0):
        return 1
    return x * exp(x, n-1)


def main():
    print("calcular x^n")

    x = int(input("valor de x:"))
    n = int(input("valor de n:"))

    ans_rec = exp(x, n)
    print(ans_rec)
    ans_iter = exp_iter(x, n)
    print(ans_iter)


if __name__ == "__main__":
    main()