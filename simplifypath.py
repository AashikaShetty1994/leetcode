"""
Question:
71. Simplify Path

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
Transform this absolute path into its simplified canonical path.

Rules:
- A single period '.' represents the current directory.
- A double period '..' represents the previous or parent directory.
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
- Any sequence of periods that is not exactly '.' or '..' is treated as a valid directory or file name.

Canonical path rules:
- The path must start with a single slash '/'.
- Directories must be separated by exactly one slash '/'.
- The path must not end with a slash '/', unless it is the root directory.
- The path must not contain '.' or '..' as path components.

Mind Map:
- simplifyPath(path)
  - data structure choice
    - Python `list` used as a stack
    - stack behavior comes from `append()` + `pop()`
    - this is LIFO: last in, first out
    - not using queue behavior here
  - split by '/'
  - process token by token
    - '' or '.' -> ignore
    - '..' -> pop from stack if possible
    - anything else -> push into stack
  - rebuild answer
    - empty stack -> '/'
    - else -> '/' + '/'.join(stack)

Why this works:
- The stack represents the current canonical path.
- Pushing means going into a directory.
- Popping means going to the parent directory.
- Ignoring '' handles repeated slashes like '//' and '///'.
- Ignoring '.' handles current-directory markers.
- Treating only exact '..' specially means '...' stays a valid folder name.
- `stack = []` is technically a Python list, but we use it like a stack.
- A Python list becomes a stack when we only use:
  - `append(x)` to push to the end
  - `pop()` to remove from the end
- That usage pattern gives LIFO behavior:
  - the last directory we entered is the first one removed by `'..'`
- This matches the path problem exactly, because parent traversal always removes the most recent valid directory.

Important Python functions used:
- path.split('/')
  - Splits the string around '/'.
  - Repeated slashes create empty strings, for example '/a//b/'.split('/')
    becomes ['', 'a', '', 'b', ''].
  - Those empty tokens are skipped.
- stack.append(part)
  - Pushes a valid directory name onto the stack.
- stack.pop()
  - Removes the most recent directory, which matches moving to parent.
  - We only call it when the stack is non-empty.
- Why `append()` + `pop()` means stack:
  - Example:
    - start with `[]`
    - `append("home")` -> `["home"]`
    - `append("user")` -> `["home", "user"]`
    - `pop()` removes `"user"`
  - The most recently added item comes out first.
  - That is stack behavior, even though the underlying container is a list.
- '/'.join(stack)
  - Combines directory names with a single slash between them.
  - Example: ['home', 'foo'] -> 'home/foo'
  - Then we add the leading slash:
    - `'/' + '/'.join(['home', 'foo'])` -> `'/home/foo'`
  - If stack is `['...', 'b', 'd']`, then:
    - `'/' + '/'.join(stack)` -> `'/.../b/d'`
- len(stack)
  - Used to detect the root case when no directories remain.

Common mapping to remember:
- Stack with list:
  - `append()` = push
  - `pop()` = pop
  - Good choice in Python
- Queue with list:
  - `append()` = enqueue
  - `pop(0)` = dequeue
  - Works, but `pop(0)` is O(n), so it is usually not preferred
- Queue with deque:
  - `append()` = enqueue
  - `popleft()` = dequeue
  - Preferred for queues because both ends are efficient

Why not queue here:
- A queue is FIFO: first in, first out.
- Path simplification needs LIFO behavior, because `'..'` removes the most recent directory, not the oldest one.
- So stack is the correct data structure, and list is a clean Python implementation of it.

Complexity:
- Time: O(n), where n is the length of the path.
  - We scan each token once and each character participates in split/join work once.
- Space: O(n)
  - In the worst case, the stack stores most of the path components.
"""

class Solution(object):
    def simplifyPath(self, path):
        # Split the path by '/' to get directory tokens (some may be empty)
        parts = path.split('/')
        # This stack will store the valid directories we keep
        stack = []
        # Loop through every token from the split
        for part in parts:
            # If it's empty or '.', it doesn't change the path
            if part == '' or part == '.':
                # Skip this token
                continue
            # If it's '..', we should go up one directory if possible
            if part == '..':
                # Only pop if we actually have a parent directory in the stack
                if len(stack) > 0:
                    # Remove the last directory because we moved up
                    stack.pop()
            else:
                # Otherwise it's a real directory name, so we keep it
                stack.append(part)
        # If nothing is in the stack, we are at root
        if len(stack) == 0:
            # Root path
            return '/'
        # Join the stack into a canonical path with single slashes
        result = '/' + '/'.join(stack)
        # Return the simplified canonical path
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        ("/a/./b/../../c/", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
        ("/", "/"),
    ]

    for path, expected in test_cases:
        actual = solution.simplifyPath(path)
        print("input =", path)
        print("expected =", expected)
        print("actual =", actual)
        print("pass =", actual == expected)
