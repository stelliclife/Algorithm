class SortingAlgorithms:
    def __init__(self, array):
        self._array = array

    @property
    def array(self):
        return self._array

    def insertion_sort_double_loop(self):
        i = 1
        length = len(self._array)

        while i < length:
            j, k = i - 1, length
            target = self._array[i]
            while j >= 0:
                if target < self._array[j]:
                    k = j
                j -= 1
            if k != length:
                temp = self._array[k:i]
                self._array[k] = target
                self._array[k+1:i+1] = temp
            i += 1

    def insertion_sort_one_loop(self):
        i, j= 1, 0
        length = len(self._array)
        k = length

        while True:
            if i == length:
                break
            target = self._array[i]
            if j < 0:
                if k != length:
                    temp = self._array[k:i]
                    self._array[k] = target
                    self._array[k+1:i+1] = temp
                i += 1
                j = i - 1
            else:
                if target < self._array[j]:
                    k = j
                j -= 1

    def selection_sort_double_loop(self):
        length = len(self._array)
        for i in range(length-1):
            k = length
            minimum = self._array[i]
            for j in range(i+1, length):
                if minimum > self._array[j]:
                    minimum = self._array[j]
                    k = j
            if k != length:
                self._array[k], self._array[i] = self._array[i], self._array[k]

    def selection_sort_one_loop(self):
        length = len(self._array)
        i, j, k = 0, 1, length
        minimum = self._array[j]

        while True:
            if minimum > self._array[j]:
                minimum = self._array[j]
                k = j
            if j != length-1:
                j += 1
            else:
                if k != length:
                    self._array[k], self._array[i] = self._array[i], self._array[k]
                k = length
                i += 1
                j = i + 1
            if i == length-1:
                break
            if j == i + 1:
                minimum = self._array[i]

    def bubble_sort_double_loop(self):
        length = len(self._array)
        range_ = range(1, length)

        for i in reversed(range_):
            for j in range(i):
                if self._array[j] > self._array[j+1]:
                    self._array[j], self._array[j+1] = self._array[j+1], self._array[j]

    def bubble_sort_one_loop(self):
        length = len(self._array)
        i, j = length-1, 0

        while True:
            if i == 0:
                break
            if self._array[j] > self._array[j+1]:
                self._array[j], self._array[j+1] = self._array[j+1], self._array[j]
            if j != i-1:
                j += 1
            else:
                i -= 1
                j = 0

    def merge_sort_top_down(self):
        return

    def merge_sort_bottom_up(self):
        return

    def quick_sort(self):
        return

    def heap_sort(self):
        return