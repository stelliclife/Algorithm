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
        return

    def bubble_sort(self):
        return

    def merge_sort(self):
        return

    def quick_sort(self):
        return

    def heap_sort(self):
        return