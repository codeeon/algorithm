

class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] > self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        largest = idx

        if left <= len(self) and self.items[left] > self.items[largest]:
            largest = left

        if right <= len(self) and self.items[right] > self.items[largest]:
            largest = right

        if largest != idx:
            self.items[idx], self.items[largest] = self.items[largest], self.items[idx]
            self._percolate_down(largest)

    def extract(self):
        if len(self) < 1:
            return 0

        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted




