class TopDownMergeSort:
    def __init__(self, array):
        self._array = array

    @property
    def array(self):
        return self._array

    def split_and_merge(self, array, left, right):
        if right - left <= 0:
            return None

        middle = int((left+right) // 2)

        self.split_and_merge(array, left, middle)
        self.split_and_merge(array, middle+1, right)
        self.merge_and_sort(array, left, middle, right)
        return None

    def merge_and_sort(self, array, left, middle, right):
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


class BottomUpMergeSort:
    def __init__(self, array):
        self._array = array