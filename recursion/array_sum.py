def array_sum(v, a, b):
    if (a == b):
        return v[a]
    return v[b] + array_sum(v, a, b-1)

def array_sum_iter(v, a, b):
    sum = 0
    for i in range(a, b+1):
        sum += v[i]
    return sum

def main():
    v = [1, 4, 45, 6, -50, 10, 2] 
    # v = [1, 0, 2, 9, 3, 9 , 4, 8, 5, 7, 6, 45]
    a = 0
    b = len(v) - 1

    res_rec = array_sum(v, a, b)
    res_iter = array_sum_iter(v, a, b)
    print(res_rec, res_iter)

if __name__ == "__main__":
    main()
