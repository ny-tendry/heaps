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
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

    def get_heap(self):
        return self.heap

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _sift_down(self, index):
        
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # Vérifie si le fils gauche est plus grand que l'élément courant
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            # Vérifie si le fils droit est plus grand que le plus grand actuel
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            # Si l'élément courant est déjà le plus grand, on arrête
            if largest == index:
                break

            # Sinon, on échange et on continue à tamiser vers le bas
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def replace_max(self, new_element):
        
        if not self.heap:
            raise IndexError("Le tas est vide.")

        max_element = self.heap[0]  # Sauvegarde de l'ancien maximum
        self.heap[0] = new_element  # Remplacement par le nouvel élément
        self._sift_down(0)          # Réorganisation du tas
        return max_element          # Retourne l'ancien maximum



