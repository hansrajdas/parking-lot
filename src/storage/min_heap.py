from parking.parking_spot import ParkingSpot


class MinHeap:
    def __init__(self, n):
        self.slots = [ParkingSpot(i + 1) for i in range(n)]

    def min_heapify(self, n, idx):
        min_idx = idx
        left_idx = 2*idx + 1
        right_idx = 2*idx + 2

        if left_idx < n and self.slots[min_idx] > self.slots[left_idx]:
            min_idx = left_idx
        if right_idx < n and self.slots[min_idx] > self.slots[right_idx]:
            min_idx = right_idx

        if min_idx != idx:
            temp = self.slots[idx]
            self.slots[idx] = self.slots[min_idx]
            self.slots[min_idx] = temp
            self.min_heapify(n, min_idx)

    def extract_min(self, n):
        self.slots[0], self.slots[n - 1] = self.slots[n - 1], self.slots[0]
        self.min_heapify(n - 1, 0)
        return self.slots[n - 1]

    def add_to_heap(self, n, spot_num):
        self.slots[n].id = spot_num
        self.slots[0], self.slots[n] = self.slots[n], self.slots[0]
        self.min_heapify(n + 1, 0)
