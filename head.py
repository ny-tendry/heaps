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
    
    def peek(self):
        """Retourne l'élément maximum sans le retirer"""
        if self.heap:
            return self.heap[0]
        return None  # ou lever une exception

    def size(self):
        """Retourne le nombre d'éléments dans le tas"""
        return len(self.heap)

    def is_empty(self):
        """Vérifie si le tas est vide"""
        return len(self.heap) == 0


# Exemple d'utilisation
if __name__ == "__main__":
    h = Heap()
    h.create_heap()
    h.build_heap([4, 10, 3, 5, 1])
    print("Tas construit:", h.get_heap())
    print("Max (peek):", h.peek())
    print("Taille:", h.size())
    print("Est vide ?", h.is_empty())
