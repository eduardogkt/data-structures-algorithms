def factors_rec(a, divisor):
    if divisor == 1:
        return [1]
    
    factors_list = factors_rec(a, divisor-1)
    
    if (a % divisor == 0):
        factors_list.append(divisor)
        
    return factors_list

def factors(a): 
    return factors_rec(a, a)

def factors_iter(a):
    factors = []
    
    for i in range(1, a+1):
        if (a % i == 0):
            factors.append(i)
    
    return factors

def main():
    a = 16
    res_rec = factors(a)
    res_iter = factors_iter(a)
    print(res_iter, res_rec)

if __name__ == "__main__":
    main()
