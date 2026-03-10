def main():
    # Input / loops / ranges
    n = 5
    print("range(n):", [i for i in range(n)])  # 0..n-1
    print("range(a, b):", [i for i in range(2, 5)])  # 2..b-1
    print("reverse range:", [i for i in range(n - 1, -1, -1)])

    # enumerate
    arr = ["a", "b", "c"]
    print(enumerate(arr))
    for i, x in enumerate(arr):
        print("enumerate:", i, x)

    # iterate pairs with zip
    a_list = [1, 2, 3]
    b_list = [10, 20, 30]
    for a, b in zip(a_list, b_list):
        print("zip pair:", a, b)

    # Lists (arrays)
    a = [1, 2, 3]
    a.append(4)
    print("append:", a)

    last = a.pop()
    print("pop last:", last, a)

    print("append:", a)
    a.append(5)
    print("append:", a)
    removed = a.pop(1)  # index
    print("pop index:", removed, a)

    print("slice copy a[i:j]:", a[0:2])
    print("reversed copy a[::-1]:", a[::-1])

    a.sort()  # in-place
    print("in-place sort:", a)

    d = [1, 4, 3]

    c = sorted(d)  # new list
    print("sorted copy:", c)


if __name__ == "__main__":
    main()
