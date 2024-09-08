def fibonacci_iter(n):
    last = 1
    last_last = 0
    
    if (n <= 1):
        return n
    
    i = 2
    while i <= n:
        curr = last_last + last
        last_last = last
        last = curr
        i += 1
    
    return curr
        
def fibonacci(n):
    if (n <= 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("fibonacci of: "))
    
    if (n < 0):
        print("negative number not allowed")
        return
    
    ans_rec = fibonacci(n)
    ans_iter = fibonacci_iter(n)

    print(ans_rec, ans_iter)


if __name__ == "__main__":
    main()