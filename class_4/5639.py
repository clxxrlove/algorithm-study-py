# https://www.acmicpc.net/problem/5639
# import sys
# sys.setrecursionlimit(10000)
#
#
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = self.right = None
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, root, key):
#         if root is None:
#             return Node(key)
#         if key > root.key:
#             root.right = self._insert(root.right, key)
#         elif key < root.key:
#             root.left = self._insert(root.left, key)
#         return root
#
#     def post_order(self):
#         self._post_order(self.root)
#
#     def _post_order(self, root):
#         if root:
#             self._post_order(root.left)
#             self._post_order(root.right)
#             print(root.key)
#
#
# tree = BST()
#
# for line in sys.stdin:
#     tree.insert(int(line.rstrip()))
#
# tree.post_order()

import sys
sys.setrecursionlimit(10 ** 5)

tree = []
for line in sys.stdin:
    tree.append(int(line.rstrip()))


def search(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            mid = i
            break

    search(start + 1, mid - 1)
    search(mid, end)
    print(tree[start])


search(0, len(tree) - 1)