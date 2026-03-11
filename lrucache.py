"""
LRU Cache mind map

Main idea:
An LRU cache must do two things very fast:
1. Find a value by key in O(1)
2. Update "most recently used" order in O(1)

To achieve that, this code combines:
1. Hash map / dictionary
   key -> node
   Fast lookup of the node for any key.

2. Doubly linked list
   Keeps usage order.
   Front  = most recently used
   Back   = least recently used

Big picture structure:

LRUCache
|- capacity
|  Maximum number of keys allowed.
|
|- cache (dict)
|  Example: {1: node1, 2: node2}
|  This gives O(1) access to nodes.
|
|- doubly linked list
|  head <-> ...real nodes... <-> tail
|  `head` and `tail` are dummy/sentinel nodes.
|  They are not real cache entries.
|  They make insert/remove logic simpler because we avoid special cases.
|
|- order meaning
|  head.next      = most recently used node
|  tail.prev      = least recently used node
|  middle nodes   = used sometime in between
|
`- key rule
   Whenever a key is used or updated, move its node to the front.

Core diagram:

head <-> [Most Recent] <-> [Less Recent] <-> [Least Recent] <-> tail
          ^
          |
      new/used node goes here

Important positions:
|- head.next = most recently used (MRU)
`- tail.prev = least recently used (LRU)

Example list state:

head <-> [3:300] <-> [1:100] <-> [2:200] <-> tail
          MRU                             LRU

Meaning:
|- key 3 was used most recently
|- key 2 was used least recently
`- if capacity is full, key 2 will be removed first

Diagram for get(1):

Before:
head <-> [3:300] <-> [1:100] <-> [2:200] <-> tail

Take node [1:100] out:
head <-> [3:300] <-> [2:200] <-> tail

Move it to the front:
head <-> [1:100] <-> [3:300] <-> [2:200] <-> tail

Diagram for put(4, 400) when capacity is full:

Before insert:
head <-> [1:100] <-> [3:300] <-> [2:200] <-> tail

Add new node to front:
head <-> [4:400] <-> [1:100] <-> [3:300] <-> [2:200] <-> tail

Now cache is too big, so evict tail.prev:
remove [2:200]

After eviction:
head <-> [4:400] <-> [1:100] <-> [3:300] <-> tail

How to think about each operation:

GET(key)
|- If key does not exist:
|  return -1
|
`- If key exists:
   1. Find node from dict
   2. Remove node from current position
   3. Add node right after head
   4. Return node.value

PUT(key, value)
|- If key already exists:
|  1. Find node
|  2. Update its value
|  3. Move it to front
|  4. Done
|
`- If key is new:
   1. Create node
   2. Save it in dict
   3. Add it to front
   4. If cache size > capacity:
      a. Least recently used node is tail.prev
      b. Remove it from list
      c. Remove its key from dict

Why the helper methods exist:
|- _remove(node)
|  Disconnects a node from the linked list.
|
`- _add_to_front(node)
   Inserts a node right after head,
   which means "this node is now most recently used".

Mental model:
Dictionary answers:
"Where is the node for this key?"

Linked list answers:
"Which key was used most recently, and which one least recently?"

Complexity:
|- __init__(capacity) -> O(1)
|- get(key)           -> O(1)
|- put(key, value)    -> O(1)
`- space              -> O(capacity)

Why O(1):
|- dict gives O(1) average key lookup
`- doubly linked list gives O(1) remove and add

That combination is the whole point of LRU cache design.

Quick memory line:
LOOKUP with dict, ORDER with linked list, EVICT from the tail.
"""


class Node:
    def __init__(self, key, value):
        # Each node stores one cache entry plus pointers for the linked list.
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # Hash map for O(1) key -> node lookup.
        self.cache = {}
        # Sentinel nodes mark the ends of the list.
        # Real cache nodes will always live between head and tail.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Unlink a node from wherever it is currently placed.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        # Insert right after head so this node becomes most recently used.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        # Missing key means cache miss.
        if key not in self.cache:
            return -1

        # Accessing a key makes it most recently used.
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        # Existing key: update value and refresh its recency.
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        # New key: create node, store it in dict, and place it at the front.
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        # If over capacity, remove the least recently used node from both
        # the linked list and the dictionary.
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


def run_tests():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("All tests passed")


if __name__ == "__main__":
    run_tests()
