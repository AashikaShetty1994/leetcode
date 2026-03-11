"""
Python essentials mind map

Think of this file in 4 blocks:

PYTHON BASICS
|- RANGE
|  `range(n)`           -> 0 to n-1
|  `range(a, b)`        -> a to b-1
|  `range(start, stop, step)`
|  Reverse example      -> `range(n - 1, -1, -1)`
|
|- ENUMERATE
|  Use when you need both:
|  1. index
|  2. value
|  Example:
|  `for i, x in enumerate(arr):`
|
|- ZIP
|  Use when you want to walk through two lists together.
|  Example:
|  `for a, b in zip(a_list, b_list):`
|
`- LIST OPERATIONS
   |- append(x)         -> add at end
   |- pop()             -> remove last item
   |- pop(i)            -> remove item at index i
   |- a[i:j]            -> slice copy
   |- a[::-1]           -> reversed copy
   |- a.sort()          -> sort in place
   `- sorted(a)         -> return a new sorted list

Complexity quick sheet:
|- range(...) loop of n items     -> O(n) to iterate / build a list from it
|- enumerate(arr)                 -> O(n) to iterate through all elements
|- zip(a, b)                      -> O(min(len(a), len(b))) to iterate fully
|- append(x)                      -> O(1) amortized
|- pop() from end                 -> O(1)
|- pop(i) from middle             -> O(n)
|- slicing a[i:j]                 -> O(k), where k is slice length
|- reverse copy a[::-1]           -> O(n)
|- a.sort()                       -> O(n log n)
`- sorted(a)                      -> O(n log n)

Quick memory line:
Range counts, enumerate indexes, zip pairs, lists store and change data.
"""


def main():
    # RANGE BASICS
    # range(n) starts at 0 and stops before n.
    n = 5
    print("range(n):", [i for i in range(n)])  # 0..n-1
    # range(a, b) starts at a and stops before b.
    print("range(a, b):", [i for i in range(2, 5)])  # 2..b-1
    # Third argument is the step. Here we walk backward.
    print("reverse range:", [i for i in range(n - 1, -1, -1)])

    # ENUMERATE
    # enumerate gives (index, value) pairs.
    arr = ["a", "b", "c"]
    print(enumerate(arr))
    for i, x in enumerate(arr):
        print("enumerate:", i, x)

    # ZIP
    # zip walks two lists together one pair at a time.
    a_list = [1, 2, 3]
    b_list = [10, 20, 30]
    for a, b in zip(a_list, b_list):
        print("zip pair:", a, b)

    # LISTS
    # append adds a new value at the end.
    a = [1, 2, 3]
    a.append(4)
    print("append:", a)

    # pop() removes and returns the last item.
    last = a.pop()
    print("pop last:", last, a)

    print("append:", a)
    a.append(5)
    print("append:", a)
    # pop(index) removes and returns the item at that index.
    removed = a.pop(1)
    print("pop index:", removed, a)

    # Slicing creates a new list from a chosen range.
    print("slice copy a[i:j]:", a[0:2])
    # a[::-1] gives a reversed copy.
    print("reversed copy a[::-1]:", a[::-1])

    # sort() changes the original list.
    a.sort()
    print("in-place sort:", a)

    d = [1, 4, 3]

    # sorted() returns a new sorted list and keeps the old one unchanged.
    c = sorted(d)
    print("sorted copy:", c)


if __name__ == "__main__":
    main()
