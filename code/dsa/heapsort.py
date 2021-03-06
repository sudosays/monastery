class Heap:

    def __init__(self, array, heap_size=-1):
        self.array = array
        self.heap_size = heap_size

    def __str__(self):
        return str(self.array)

    def left_of(index):
        return (2*index + 1)

    def right_of(index):
        return (2*index + 2)
    
    def _swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def _max_heapify(self, index):
        left = Heap.left_of(index)
        right = Heap.right_of(index)
    
        largest = index

        if left < self.heap_size:
            if self.array[left] > self.array[largest]:
                largest = left
                
        if right < self.heap_size:
            if self.array[right] > self.array[largest]:
                largest = right

        if largest != index:
            self._swap(largest, index)
            self._max_heapify(largest)
        else:
            return
    
    def _build_max_heap(self):
        self.heap_size = len(self.array)

        for i in range(self.heap_size//2, -1, -1):
            self._max_heapify(i)
    
    def sort(self):
        self._build_max_heap()

        for i in range(len(self.array)-1,0,-1):
            self._swap(i,0)
            self.heap_size -= 1
            self._max_heapify(0)

if __name__ == "__main__":

    case_numbers = [
        20200127223412001,
        20200212000201001,
        20200128141212003,
        20200205130501001,
        20200204221331001,
        20200126161212001,
        20200206184812001,
        20200131200531002,
        20200128134516001,
        20200125103945001,
        20200128134612002,
        20200131144454001
    ]

    h = Heap(case_numbers)
    
    h.sort()
    
    print(h)

