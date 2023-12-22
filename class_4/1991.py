# https://www.acmicpc.net/problem/1991
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, left, right):
        if self.root is None:
            self.root = Node(key)

        self._insert(self.root, key, left, right)

    def _insert(self, root, key, left, right):
        if root.key == key:
            if right != ".":
                root.right = Node(right)
            if left != ".":
                root.left = Node(left)
        else:
            if root.right:
                self._insert(root.right, key, left, right)
            if root.left:
                self._insert(root.left, key, left, right)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, root):
        if root:
            print(root.key, end="")
            self._pre_order(root.left)
            self._pre_order(root.right)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.key, end="")
            self._in_order(root.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, root):
        if root:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.key, end="")


N = int(sys.stdin.readline().rstrip())
tree = Tree()

for _ in range(N):
    p, l, r = sys.stdin.readline().split()
    tree.insert(p, l, r)

tree.pre_order()
print()
tree.in_order()
print()
tree.post_order()