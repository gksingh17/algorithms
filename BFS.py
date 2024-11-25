'''
    start at root node and add it to queue
    while queue not empty 
        deque the front node (popleft)
        visit the node (process)
        enqueue all it's child nodes (left, right)
    Repeat until all nodes are visited
'''

from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        # enqueue if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print("Bfs Traversal")
bfs(root)
