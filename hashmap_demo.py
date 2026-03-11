"""
Python dict mind map

Think: MAKE -> SEE -> CHANGE -> CHECK -> WALK -> JOIN -> REMOVE -> SAFE DEFAULT

1. MAKE
   `scores = {"alice": 90, "bob": 75}`
   Create the hashmap.

2. SEE
   `scores["alice"]`
   `scores.get("dave", "not found")`
   Read a value. Use `get()` when the key may be missing.

3. CHANGE
   `scores["dave"] = 82`
   `scores["bob"] = 80`
   Same syntax for insert and update.

4. CHECK
   `"cara" in scores`
   Test whether a key exists.

5. WALK
   `for name, score in scores.items():`
   Iterate through key-value pairs.

6. JOIN
   `{**scores, **extra}`
   `scores.update(other_dict)`
   Combine two dictionaries.

7. REMOVE
   `scores.pop("alice")`
   Delete a key and get its removed value back.

8. SAFE DEFAULT
   `visits.setdefault("home", 0)`
   Create a starting value only if the key is missing.

Complexity guide for Python dict (average case):
|- create / access / insert / update / membership / delete -> O(1)
|- iterate through all items                           -> O(n)
|- merge / update with another dict of size m          -> O(m)
`- space                                              -> O(n)

Note:
Python dict uses hashing, so these are average-case costs.
Worst-case lookup can degrade, but that is uncommon in normal use.

Quick memory line:
Create it, see it, change it, check it, walk it, join it, remove it, protect it.
"""


def create_scores():
    return {"alice": 90, "bob": 75, "cara": 88}


def show_starting_dict(scores):
    print("Initial:", scores)


def demo_read_values(scores):
    print("alice:", scores["alice"])
    print("dave with default:", scores.get("dave", "not found"))


def demo_write_values(scores):
    scores["dave"] = 82
    scores["bob"] = 80
    print("After insert/update:", scores)


def demo_check_key(scores):
    print("cara in scores?", "cara" in scores)


def demo_loop_items(scores):
    for name, score in scores.items():
        print(name, "->", score)


def demo_combine_with_merge(scores):
    extra = {"erin": 91, "bob": 83}
    merged = {**scores, **extra}
    print("Merged:", merged)


def demo_combine_with_update(scores):
    scores.update({"bob": 99, "fran": 77})
    print("After update:", scores)


def demo_remove_key(scores):
    removed = scores.pop("alice")
    print("Removed alice:", removed)
    print("After delete:", scores)


def demo_default_value():
    visits = {}
    visits.setdefault("home", 0)
    print("Visits:", visits)
    visits["home"] += 1
    print("Visits:", visits)


def main():
    scores = create_scores()
    show_starting_dict(scores)

    demos = [
        demo_read_values,
        demo_write_values,
        demo_check_key,
        demo_loop_items,
        demo_combine_with_merge,
        demo_combine_with_update,
        demo_remove_key,
    ]

    for demo in demos:
        demo(scores)

    demo_default_value()


if __name__ == "__main__":
    main()
