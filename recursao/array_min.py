# def array_min(v, a, b):
#     if (a == b):
#         return a

#     if (v[a] < v[b]):
#         return array_min(v, a, b-1)
#     else:
#         return array_min(v, a+1, b)

def array_min(v, a, b):
    if (a == b):
        return a

    min = array_min(v, a, b-1)

    if (v[b] < v[min]):
        min = b

    return min

def array_min_iter(v, a, b):
    min = a

    for i in range(a+1, b+1):
        if (v[i] < v[min]):
            min = i

    return min

def main():
    v = [1, 4, 45, 6, -50, 10, 2]
    # v = [1, 0, 2, 9, 3, 9 , 4, 8, 5, 7, 6, 45]
    a = 0
    b = len(v) - 1

    res_rec = array_min(v, a, b)
    res_iter = array_min_iter(v, a, b)
    print(res_rec, res_iter)

if __name__ == "__main__":
    main()
