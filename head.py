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

    # Ajout:sift_down(reutilisable pour suppression)
    def sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    # Ajout:extract_max
    def extract_max(self):
        if self.is_empty():
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return max_value
    
# créer une fonction execute pour faciliter la création de heap lors de l'insertion des nombre un à un    
def execute(self):
    h = Heap()
    h.create_heap()
    h.build_heap(self)
    print("\nTas construit:", h.get_heap())
    print("Max (peek):", h.peek())
    print("Taille:", h.size())
    print("Est vide ?", h.is_empty(), "\n")

def insertion_et_sift_up():
    liste = []
    while True:
        print("Entrer un nombre (ou 's' pour supprimer le max, ou vide pour quitter):")
        element = input()
        if element == "":
            break
        elif element.lower() == "s":
            h = Heap()
            h.build_heap(liste)
            removed = h.extract_max()
            liste = h.get_heap()
            print(f"Max supprimé: {removed}")
            print("Tas après suppression:", liste)
        else:
            liste.append(int(element))
            execute(liste)
insertion_et_sift_up()    
