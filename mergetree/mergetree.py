import sys


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


class MergeSortTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = [0] * (len(arr) * 4)
        self.build_merged_tree(arr, 1, 0, len(arr) - 1)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return merge(left, right)

    def build_merged_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = [arr[start]]
            return

        mid = (start + end) // 2
        self.build_merged_tree(arr, node * 2, start, mid)
        self.build_merged_tree(arr, node * 2 + 1, mid + 1, end)

        self.tree[node] = merge(self.tree[2 * node], self.tree[2 * node + 1])

    def search(self, left, right, value):
        left -= 1
        right -= 1

        def upper_bound(length, idx):
            start, end = 0, length
            while start < end:
                mid = (start + end) // 2
                if self.tree[idx][mid] <= value:
                    start = mid + 1
                else:
                    end = mid
            return len(self.tree[idx]) - end

        def _search(start, end, idx):
            if right < start or left > end:
                return 0
            if left <= start and end <= right:
                return upper_bound(len(self.tree[idx]), idx)
            mid = (start + end) // 2
            lvalue = _search(start, mid, idx * 2)
            rvalue = _search(mid + 1, end, idx * 2 + 1)
            return lvalue + rvalue

        print(_search(0, self.length - 1, 1))

    def get_tree(self):
        return self.tree


N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))
tree = MergeSortTree(arr)

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    tree.search(a, b, c)