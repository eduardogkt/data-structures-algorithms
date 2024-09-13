def palindrome(v, a, b):
    # n <= 1
    if ((b-a+1) <= 1):
        return True

    is_palindrome = palindrome(v, a+1, b-1)
    if (is_palindrome and v[a] == v[b]):
        return True
    else:
        return False

def main():
    v = [0, 1, 2, 3, 2, 1, 0]
    a = 0
    b = len(v) - 1

    res_rec = palindrome(v, a, b)
    print(res_rec)


if __name__ == "__main__":
    main()
