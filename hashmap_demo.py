def main():
    # Create a hashmap (Python dict)
    scores = {"alice": 90, "bob": 75, "cara": 88}
    print("Initial:", scores)

    # Read
    print("alice:", scores["alice"])
    print("dave with default:", scores.get("dave", "not found"))

    # Insert / update
    scores["dave"] = 82
    scores["bob"] = 80
    print("After insert/update:", scores)

    # Check membership
    print("cara in scores?", "cara" in scores)

    # Delete
    removed = scores.pop("alice")
    print("Removed alice:", removed)
    print("After delete:", scores)

    # Iterate
    for name, score in scores.items():
        print(name, "->", score)

    # Safe update with setdefault
    visits = {}
    visits.setdefault("home", 0)
    visits["home"] += 1
    print("Visits:", visits)

    # Merge two dicts
    extra = {"erin": 91, "bob": 83}
    merged = {**scores, **extra}
    print("Merged:", merged)

    # Update with another dict
    scores.update({"bob": 99, "fran": 77})
    print("After update:", scores)


if __name__ == "__main__":
    main()
