'''
Convert array into minimum heap
Task. The first step of the HeapSort algorithm is to create a heap
      from the array you want to sort. By the way, did you know that
      algorithms based on Heaps are widely used for external sort,
      when you need to sort huge files that don’t fit into memory of a computer?
      Your task is to implement this first step and convert a given array
      of integers into a heap. You will do that by applying a certain
      number of swaps to the array. Swap is an operation which exchanges
      elements ai and aj of the array a for some i and j. You will need to convert
      the array into a minimum heap using only 𝑂(n) swaps.
Input Format. The first line of the input contains single integer n.
              The next line contains n space-separated integers ai.
Output Format. The first line of the output should contain single integer
               m — the total number of swaps. m must satisfy conditions
               0 <= m <= 4n. The next m lines should contain the swap
               operations used to convert the array a into a heap.
'''

import math


class HeapBuilder:
    def __init__(self):
        self.swaps = []
        self.data = []
        self.heap = []
        self.size = 0
    
    def read_data(self):
        n = int(input())
        self.data = [int(s) for s in input().split()]
        self.size = n
    
    def write_response(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, index):
        element = self.data[index]
        left_index, right_index = 2 * index + 1, 2 * index + 2
        left_element = self.data[left_index] if left_index < self.size else math.inf
        right_element = self.data[right_index] if right_index < self.size else math.inf
        if left_element == math.inf and right_element == math.inf:
            return
        min_element = min(left_element, right_element)
        min_index = left_index if min_element == left_element else right_index
        if element > min_element:
            self.do_swap(index, min_index)
            self.sift_down(min_index)

    def do_swap(self, i, j):
        self.swaps.append([i, j])
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


heap_builder = HeapBuilder()
heap_builder.solve()
