import bisect


"""
SnapshotArray mind map

Main idea:
This data structure stores array values across many snapshots.
Instead of copying the whole array on every snap, it stores only changes.

Core concept:
For each index, keep a history list of:
`(snap_id, value)`

So each index remembers:
"At snapshot X, what was my value?"

Structure:

SnapshotArray
|- snap_id
|  The id that will be assigned to the next snapshot.
|
`- history
   A list with one history list per array index.

Diagram:

history[0] = [(0, 0), (2, 5), (4, 9)]
history[1] = [(0, 0)]
history[2] = [(0, 0), (1, 7)]

Meaning:
|- index 0 had value 0 from snap 0 onward
|- at snap 2, index 0 changed to 5
|- at snap 4, index 0 changed to 9
`- index 1 was never changed, so it stayed 0

How each operation works:

SET(index, val)
|- Look at the history list for that index
|- If the last saved pair already belongs to current snap_id:
|  update that pair
|  Reason: multiple sets before one snap should keep only the newest value
`- Otherwise append a new pair `(snap_id, val)`

SNAP()
|- Return current snap_id
`- Then increment it for the next snapshot

GET(index, snap_id)
|- Look at the history list for that index
|- Find the rightmost pair whose saved snap_id <= requested snap_id
`- Return that pair's value

Binary search diagram for get(index, snap_id):

history[0] = [(0, 0), (2, 5), (4, 9)]

get(0, 3)
|- snap 3 is not stored exactly
|- we need the latest change at or before 3
`- answer comes from (2, 5), so return 5

Why bisect_right is used:
It finds the insertion point to the right of all valid pairs.
Then we step back by 1 to get the last snapshot <= requested one.

Complexity:
|- __init__(length)  -> O(length)
|- set(index, val)   -> O(1) amortized
|- snap()            -> O(1)
`- get(index, snap_id) -> O(log k)
   where k = number of saved changes for that index

Space:
O(length + total number of recorded updates)

Quick memory line:
Do not copy the whole array. Store only changes, then binary-search history.
"""


class SnapshotArray(object):
    def __init__(self, length):
        self.snap_id = 0
        # history[i] holds (snap_id, value) pairs for index i.
        self.history = []
        for i in range(length):
            self.history.append([(0, 0)])

    def set(self, index, val):
        hist = self.history[index]
        # If we already changed this index in the current snapshot window,
        # overwrite that pending value instead of appending another pair.
        if hist[-1][0] == self.snap_id:
            hist[-1] = (self.snap_id, val)
        else:
            hist.append((self.snap_id, val))

    def snap(self):
        # Return the current snapshot id, then advance to the next one.
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
