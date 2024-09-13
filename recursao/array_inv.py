def array_inv(v, a, b):
    if (a > b):
        return v

    aux = v[b]
    v[b] = v[a]
    v[a] = aux

    return array_inv(v, a+1, b-1)

def array_inv_iter(v, a, b):
    j = 0
    v_inv = list(range(len(v)))
 
    for i in range(b, a-1, -1):
        v_inv[j] = v[i]
        j += 1

    return v_inv

def main():
    # v = [1, 4, 45, 6, -50, 10, 2] 
    # v = [1, 0, 2, 9, 3, 9 , 4, 8, 5, 7, 6, 45]
    v = [0, 1, 2, 3, 4, 5]
    a = 0
    b = len(v) - 1

    res_iter = array_inv_iter(v, a, b)
    res_rec = array_inv(v, a, b)
    print(res_rec, res_iter)

if __name__== "__main__":
    main()
            