"""
Trie mind map

Main idea:
A trie stores words character by character.
Each path from root through child nodes represents a prefix.

Why use a trie:
|- fast prefix checks
|- natural word-by-word insertion
`- avoids scanning every stored word for prefix queries

Structure:

Trie
`- root
   `- children by character

TrieNode
|- children : dict
|  Maps one character to the next node
`- is_end : bool
   True means "a complete word ends here"

Diagram:

Insert "apple" and "app"

root
`- a
   `- p
      `- p (is_end = True for "app")
         `- l
            `- e (is_end = True for "apple")

Important idea:
Every word is a prefix path,
but not every prefix is automatically a full word.

That is why `is_end` matters:
|- Path for "app" may exist
`- but search("app") is only True if that node has is_end = True

How operations work:

INSERT(word)
|- Start at root
|- For each character:
|  |- if child does not exist, create it
|  `- move to that child
`- Mark final node as is_end = True

SEARCH(word)
|- Start at root
|- Walk character by character
|- If any character path is missing: return False
`- After the walk, return node.is_end

STARTSWITH(prefix)
|- Start at root
|- Walk character by character
|- If any character path is missing: return False
`- If the path exists fully: return True

Search vs startsWith:
|- search("app") checks:
|  "Does the full word end here?"
`- startsWith("app") checks:
   "Does this path exist at all?"

Complexity:
Let n = length of the word or prefix.

|- insert(word)        -> O(n)
|- search(word)        -> O(n)
|- startsWith(prefix)  -> O(n)
`- Extra space for insert -> O(n) in the worst case
   if every character creates a new node

Quick memory line:
Trie = character path tree. Walk letters. Mark full words with is_end.
"""


class TrieNode:
    def __init__(self):
        # children stores the next possible characters.
        self.children = {}
        # is_end marks whether a complete word ends at this node.
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            # Create missing path one character at a time.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # The final node represents a complete stored word.
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # True only if a complete word ends here.
        return node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # If the whole prefix path exists, the answer is True.
        return True


# Simple tests (run after you implement the methods)
def run_tests():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startsWith("app") is True
    t.insert("app")
    assert t.search("app") is True
    print("All tests passed")

run_tests()
