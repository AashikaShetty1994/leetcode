def main():
    a = {1, 2, 3, 4}
    b = {3, 4, 5}

    print("a:", a)
    print("b:", b)

    # Union
    print("union:", a | b)

    # Intersection
    print("intersection:", a & b)

    # Difference
    print("difference a-b:", a - b)
    print("difference b-a:", b - a)

    # Symmetric difference
    print("symmetric difference:", a ^ b)

    # Subset / superset
    c = {3, 4}
    print("c:", c)
    print("c subset of a?", c <= a)
    print("a superset of c?", a >= c)

    # Disjoint
    d = {7, 8}
    print("d:", d)
    print("a disjoint with d?", a.isdisjoint(d))

    # Add / remove / discard / pop / clear
    e = {1, 2}
    print("e start:", e)
    e.add(3)
    print("e after add:", e)
    e.remove(2)
    print("e after remove:", e)
    e.discard(9)
    print("e after discard missing:", e)
    popped = e.pop()
    print("e popped:", popped, "remaining:", e)
    e.clear()
    print("e after clear:", e)

    # In-place updates
    f = {1, 2, 3}
    f |= {3, 4}
    print("f after |=:", f)
    f &= {2, 3}
    print("f after &=:", f)
    f -= {2}
    print("f after -=:", f)
    f ^= {3, 5}
    print("f after ^=:", f)


if __name__ == "__main__":
    main()
