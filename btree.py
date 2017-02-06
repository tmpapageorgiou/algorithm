# coding: UTF-8

INF = float("inf")

class BTree:

    def __init__(self, data):
        self._data = data
        self.tree_size = 2 * len(data) -1

        self._tree = self.tree_size * [self.LIMIT]
        self._rebuild()


    def _rebuild(self):

        def recursive(low, high, pos):

            if pos >= self.tree_size:
                return

            if low == high:
                self._tree[pos] = self._data[low]
                return

            mid = (low + high) / 2
            recursive(low, mid, 2*pos+1)
            recursive(mid+1, high, 2*pos+2)
            self._tree[pos] = self._compare(self._left_child(pos),
                                            self._right_child(pos))

        return recursive(0, len(self._data)-1, 0)

    def _left_child(self, pos):
        return self._tree[2*pos+1] if 2*pos+1 < self.tree_size else self.LIMIT

    def _right_child(self, pos):
        return self._tree[2*pos+2] if 2*pos+2 < self.tree_size else self.LIMIT

    def query(self, qlow, qhigh):

        def recursion(low, high, pos):

            if qlow > high or qhigh < low:
                return self.LIMIT
            elif qlow <= low and qhigh >= high :
                return self._tree[pos] if pos < self.tree_size else self.LIMIT
            else:
                mid = (low+high)/2
                return self._compare(recursion(low, mid, pos*2+1),
                                     recursion(mid+1, high, pos*2+2))
        return recursion(0, len(self._data)-1, 0)

class MinBTree(BTree):

    LIMIT = INF

    def _compare(self, *args):
        return min(*args)

class MaxBTree(BTree):
    LIMIT = -INF

    def _compare(self, *args):
        return max(*args)

class SumBTree(BTree):
    LIMIT = 0

    def _compare(self, *args):
        return sum(args)
