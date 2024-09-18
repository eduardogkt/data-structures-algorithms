def array_mean(v, a, b):
    if (a == b):
        return v[a]

    subarray_sum = (b-a) * array_mean(v, a, b-1)
    
    return (v[b] + subarray_sum) / (b-a+1)

def array_mean_iter(v, a, b):
    sum = 0
    for i in range(a, b+1):
        sum += v[i]

    return sum / (b-a+1)

def main():
    v = [1, 2, 3, 3, 1, 3, 2]
    a = 0
    b = len(v) - 1

    res_rec = array_mean(v, a, b)
    res_iter = array_mean_iter(v, a, b)
    print(res_rec, res_iter)


if __name__ == "__main__":
    main()
