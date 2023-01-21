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

    def top_down_merge_sort(self, array, left, right):
        if right - left <= 0:
            return None

        middle = int((left+right) // 2)

        self.top_down_merge_sort(array, left, middle)
        self.top_down_merge_sort(array, middle+1, right)
        self._merge_and_sort(array, left, middle, right)
        return None

    def bottom_up_merge_sort(self, array):
        length = len(array)
        width, k = 1, 0

        while width <= length:
            k = 0
            width *= 2
            while k < length:
                left = k
                right = k + width - 1
                middle = right - (width//2)
                if right > length-1:
                    right = length - 1
                self._merge_and_sort(array, left, middle, right)
                k += width

    def _merge_and_sort(self, array, left, middle, right):
        left_ = array[left:middle+1]
        right_ = array[middle+1:right+1]
        i, j = 0, 0
        for k in range(left, right+1):
            if left_ and right_:
                if left_[i] < right_[j]:
                    self._array[k] = left_[i]
                    left_.pop(i)
                else:
                    self._array[k] = right_[j]
                    right_.pop(j)
            else:
                if left_:
                    self._array[k] = left_[i]
                    left_.pop(i)
                else:
                    self._array[k] = right_[j]
                    right_.pop(j)

    def quick_sort(self, array, left, right):
        i, j = -1, 0
        pivot = array[right]
        if left >= right:
            return None

        while j <= right:
            if j == i:
                j += 1
            if j == right:
                i += 1
                array[i], array[j] = array[j], array[i]
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
            else:
                j += 1
        self._array = array
        k = array.index(pivot)

        self.quick_sort(array, left, k-1)
        self.quick_sort(array, k+1, right)

    def heap_sort(self):
        return