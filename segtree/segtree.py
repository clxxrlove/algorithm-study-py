import sys
from math import ceil, log2

data = list(map(int, sys.stdin.readline().split()))


class SegTree:
    k = 0
    tree = []
    func = {'sum': lambda x, y: x + y, 'min': min, 'max': max}

    def __init__(self, _data, _type):
        self.func = self.func[_type]
        self.k = ceil(log2(len(_data)))
        tree_size = pow(2, self.k + 1)

        self.tree = [0] * tree_size

        pointer = tree_size // 2

        for d in _data:
            self.tree[pointer] = d
            pointer += 1

    def _segmentify(self):
        tree_size = pow(2, self.k + 1)

        for i in range(tree_size - 1, 1, -1):
            if self.func == min and i % 2 == 0:
                self.tree[i // 2] = self.tree[i]
            else:
                self.tree[i // 2] = self.func(self.tree[i // 2], self.tree[i])

    def segmentify(self):
        self._segmentify()

    def query(self, start, end):
        k = pow(2, self.k)

        return self._query(start + k, end + k)

    def _query(self, start, end):
        result = 0
        if self.func == min:
            result = float('inf')

        while True:
            if start % 2 == 1:
                result = self.func(result, self.tree[start])
            if end % 2 == 0:
                result = self.func(result, self.tree[end])

            start = (start + 1) // 2
            end = (end - 1) // 2

            if start > end:
                break

        return result

    def update(self, index, element):
        self.tree[index + pow(2, self.k)] = element
        self._update((index + pow(2, self.k)) // 2, element)

    def _update(self, index, element):
        while index > 0:
            self.tree[index] += element
            index //= 2

    def get_tree(self):
        return self.tree


tree = SegTree(data, 'sum')