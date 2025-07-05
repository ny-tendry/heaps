class Heap:
    def __init__(self):
        self.heap = []

    def create_heap(self):
        self.heap = []

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)

    def build_heap(self, array):
        self.heap = array[:]
        n = len(self.heap)

        # Commencer par le dernier noeud parent
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def get_heap(self):
        return self.heap


# Exemple d'utilisation
if __name__ == "__main__":
    h = Heap()
    h.create_heap()
    h.build_heap([4, 10, 3, 5, 1])
    print("Tas construit:", h.get_heap())
