class MergeSortWithInsertion:
    def __init__(self, cutoff=7):
        # subarray의 숫자 => cutoff( 기본으로 10 / 7 등이 적절)
        self.cutoff = cutoff

    def insertion_sort(self, arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(self, arr, low, mid, high):
        left, right = arr[low:mid + 1], arr[mid + 1:high + 1]
        i = j = 0
        for k in range(low, high + 1):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

    def merge_sort(self, arr, low, high):
        """
        재귀적으로 insertions sort을 할 cutoff 이하로만 array를 나눠서, insertion sort을 하고 merge 합니다.
        """
        if high - low + 1 <= self.cutoff:  # Use insertion sort for small subarrays
            self.insertion_sort(arr, low, high)
            return

        mid = (low + high) // 2
        # 재귀적으로 자기 자신 함수 객체 호출(명령을 받는 객체(self)의 cutoff보다 큰 범위까지만 merge_sort() 호출,
        # 그 이하부터는 insertion_sort() 처리
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def sort(self, arr):
        """
        Sort할 array를 merge + insertion sort를 합니다.
        """
        self.merge_sort(arr, 0, len(arr) - 1)
        return arr
