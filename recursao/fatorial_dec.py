def fat_dec_iter(n, k):
    answer = 1
    i = n - k + 1
    while i <= n:
        answer *= i
        i += 1
    return answer

def fat_dec(n, k):
    if k == 1:
        return n
    else:
        return n * fat_dec(n-1, k-1)

def main():
    print("factorial from n to k")
    k = int(input("k: "))
    n = int(input("n: "))
    
    if (n < 0 or k < 0):
        print("n and k can't be negative")
        return
    
    if (n < k):
        print("n can't be less than k")
        return
    
    ans_rec = fat_dec(n, k)
    ans_iter = fat_dec_iter(n, k)

    print(f"rec {ans_rec}")
    print(f"iter {ans_iter}")
    

if __name__ == "__main__":
    main()