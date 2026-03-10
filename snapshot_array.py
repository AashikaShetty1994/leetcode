import bisect


class SnapshotArray(object):
    def __init__(self, length):
        self.snap_id = 0
        # history[i] holds (snap_id, value) pairs for index i.
        self.history = []
        for i in range(length):
            self.history.append([(0, 0)])

    def set(self, index, val):
        hist = self.history[index]
        if hist[-1][0] == self.snap_id:
            hist[-1] = (self.snap_id, val)
        else:
            hist.append((self.snap_id, val))

    def snap(self):
        curr = self.snap_id
        self.snap_id += 1
        return curr

    def get(self, index, snap_id):
        hist = self.history[index]
        # Rightmost pair with snap_id <= requested.
        idx = bisect.bisect_right(hist, (snap_id, float("inf")))
        pos = idx - 1
        return hist[pos][1]


def run_tests():
    # Example 1
    arr = SnapshotArray(3)
    arr.set(0, 5)
    snap_id = arr.snap()
    assert snap_id == 0
    arr.set(0, 6)
    assert arr.get(0, 0) == 5

    # Multiple sets before snap
    arr = SnapshotArray(1)
    arr.set(0, 1)
    arr.set(0, 2)
    assert arr.snap() == 0
    assert arr.get(0, 0) == 2

    # Unset index returns default 0
    arr = SnapshotArray(2)
    assert arr.snap() == 0
    assert arr.get(1, 0) == 0

    # Later snapshots
    arr = SnapshotArray(2)
    arr.set(1, 7)
    s0 = arr.snap()
    arr.set(1, 9)
    s1 = arr.snap()
    assert arr.get(1, s0) == 7
    assert arr.get(1, s1) == 9

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
