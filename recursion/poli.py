def exp(x, n): # x^n
    if (n == 0):
        return 1
    return x * exp(x, n-1)

# p(a, b, x) = p[a]*x^0 + p[a+1]*x^1 + ... + p[b]x^(b−a)
# p(a, b, x) = p[b]x^(b−a) + ... + p[a+1]*x^1 + p[a]*x^0
def poli(v, a, b, x):
    if (a == b):
        print(f"{v[b]}×{x}^0")
        return v[b]*x
    
    print (f"{v[b]}×{x}^{b-a} + ", end="")
    return v[b] * exp(x, b-a) + poli(v, a, b-1, x)

def main():
    v = [4, 8, 15, 16, 23, 42]
    a = 0
    b = len(v) - 1
    x = 1
    # a=2, b=4, x=1, poli(v, a, b, x)=54
    
    res_rec = poli(v, a, b, x)
    print(res_rec)


if __name__ == "__main__":
    main()