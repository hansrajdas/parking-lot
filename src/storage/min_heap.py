from parking.parking_spot import ParkingSpot


class MinHeap:
    def __init__(self, n):
        self.slots = [ParkingSpot(i + 1) for i in range(n)]

    def min_heapify(self, n, idx):
        """Min heapfies parking slots based on ids."""
        min_idx = idx
        left_idx = 2*idx + 1
        right_idx = 2*idx + 2

        if left_idx < n and self.slots[min_idx].id > self.slots[left_idx].id:
            min_idx = left_idx
        if right_idx < n and self.slots[min_idx].id > self.slots[right_idx].id:
            min_idx = right_idx

        if min_idx != idx:
            temp = self.slots[idx]
            self.slots[idx] = self.slots[min_idx]
            self.slots[min_idx] = temp
            self.min_heapify(n, min_idx)

    def shift_up(self, node_idx):
        """Shits node up in heap if new element added breaks heap property."""
        if node_idx:
            parent_idx = (node_idx - 1)/2
            if self.slots[parent_idx].id > self.slots[node_idx].id:
                buf = self.slots[parent_idx]
                self.slots[parent_idx] = self.slots[node_idx]
                self.slots[node_idx] = buf
                self.shift_up(parent_idx)

    def extract_min(self, n):
        """Extracts and returns min parking slot number from free slots."""
        self.slots[0], self.slots[n - 1] = self.slots[n - 1], self.slots[0]
        self.min_heapify(n - 1, 0)
        return self.slots[n - 1]

    def add_to_heap(self, n, spot_num):
        """Adds a new parking spot to heap."""
        self.slots[n].id = spot_num
        self.shift_up(n)
