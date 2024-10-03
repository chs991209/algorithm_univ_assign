class InsertionSort:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def sort(self):
        # Traverse from 1 to len(self._data)
        for i in range(1, len(self._data)):
            key = self._data[i]
            j = i - 1
            while j >= 0 and self._data[j] > key:
                self._data[j + 1] = self._data[j]
                j -= 1
            self._data[j + 1] = key
        return self._data
