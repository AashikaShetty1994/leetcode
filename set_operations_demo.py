"""
Python set mind map

Main idea:
A set stores unique values.
Use it when you care about membership, overlap, uniqueness, and fast lookups.

Complexity note:
Average-case membership, add, remove, and discard are O(1)
because Python sets are hash-based.
Operations that compare or combine sets usually depend on set sizes.

Think in 4 memory blocks:

SET
|- LOOK AT RELATIONSHIPS BETWEEN SETS
|  |- union                  -> `a | b`              -> O(len(a) + len(b))
|  |  Everything from both sets.
|  |
|  |- intersection           -> `a & b`              -> O(min(len(a), len(b)))
|  |  Only common values.
|  |
|  |- difference             -> `a - b`              -> O(len(a))
|  |  Values in a but not in b.
|  |
|  `- symmetric difference   -> `a ^ b`              -> O(len(a) + len(b))
|     Values in exactly one of the sets.
|
|- CHECK LOGICAL RELATIONSHIPS
|  |- subset                 -> `c <= a`             -> O(len(c))
|  |- superset               -> `a >= c`             -> O(len(c))
|  `- disjoint               -> `a.isdisjoint(d)`    -> O(min(len(a), len(d)))
|
|- CHANGE ONE SET
|  |- add(x)                 -> add one value        -> O(1) average
|  |- remove(x)              -> remove, error if missing -> O(1) average
|  |- discard(x)             -> remove, no error if missing -> O(1) average
|  |- pop()                  -> remove one random item -> O(1) average
|  `- clear()                -> remove everything    -> O(len(set))
|
`- UPDATE IN PLACE
   |- `|=`  union update              -> O(len(other))
   |- `&=`  intersection update       -> O(min(len(set), len(other)))
   |- `-=`  difference update         -> O(len(other))
   `- `^=`  symmetric difference update -> O(len(set) + len(other))

Quick memory line:
Sets compare, filter, and clean unique values.
"""


def main():
    # Two starting sets for comparison operations.
    a = {1, 2, 3, 4}
    b = {3, 4, 5}

    print("a:", a)
    print("b:", b)

    # UNION: everything from both sets.
    print("union:", a | b)

    # INTERSECTION: only values common to both.
    print("intersection:", a & b)

    # DIFFERENCE: values in the first set but not the second.
    print("difference a-b:", a - b)
    print("difference b-a:", b - a)

    # SYMMETRIC DIFFERENCE: values in exactly one set.
    print("symmetric difference:", a ^ b)

    # SUBSET / SUPERSET checks.
    c = {3, 4}
    print("c:", c)
    print("c subset of a?", c <= a)
    print("a superset of c?", a >= c)

    # DISJOINT means the two sets have nothing in common.
    d = {7, 8}
    print("d:", d)
    print("a disjoint with d?", a.isdisjoint(d))

    # BASIC SET CHANGES.
    e = {1, 2}
    print("e start:", e)
    # add inserts a new value.
    e.add(3)
    print("e after add:", e)
    # remove deletes a value, but fails if it is missing.
    e.remove(2)
    print("e after remove:", e)
    # discard deletes a value safely, even if it is absent.
    e.discard(9)
    print("e after discard missing:", e)
    # pop removes one arbitrary value.
    popped = e.pop()
    print("e popped:", popped, "remaining:", e)
    # clear removes all values.
    e.clear()
    print("e after clear:", e)

    # IN-PLACE UPDATES modify the same set directly.
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
