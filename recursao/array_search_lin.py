def array_search_lin(v, a, b, x):
    if (a > b):
        return None

    if (v[b] == x):
        return b

    return array_search_lin(v, a, b-1, x)

def array_search_lin_iter(v, a, b, x):
    for i in range(a, b+1):
         if (v[i] == x):
            return i

    return None

def main():
    v = [54, -9, 6, 34, 5, 2, 28, 234, -3]
    a = 0
    b = len(v) - 1
    x = 28

    res_rec = array_search_lin(v, a, b, x)
    res_iter = array_search_lin_iter(v, a, b, x)
    print(res_rec, res_iter)
 
if __name__ == "__main__":
    main()
