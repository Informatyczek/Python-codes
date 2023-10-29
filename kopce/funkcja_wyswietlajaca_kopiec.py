import heapq
import time
def print_tree(heap):
    """
    This function print 1-dimension array in tree view, this is little help
    for heap visualisation in CLI, may not work properly for big heaps
    with negative numbers...
    :param heap: heapq.heap
    """
    max_depth = 0
    node_to_depth = {}
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            node_to_depth[left] = node_to_depth.get(i, 0) + 1
            max_depth = max(max_depth, node_to_depth[left])
        if right < len(heap):
            node_to_depth[right] = node_to_depth.get(i, 0) + 1
            max_depth = max(max_depth, node_to_depth[right])
        node_to_depth[i] = node_to_depth.get(i, 0)

    for depth in range(max_depth + 1):
        nodes = [i for i in node_to_depth if node_to_depth[i] == depth]
        nodes.sort()
        spaces = 2 ** (max_depth - depth + 1) - 1
        line = ""
        for i in nodes:
            line += " " * spaces + str(heap[i])
            spaces = 2 * spaces + 1
        print(line + '\n')

def min_heapify(heap, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest, n)
def build_min_heap(heap):
    n = len(heap)
    start_index = (n // 2) - 1

    for i in range(start_index, -1, -1):
        min_heapify(heap, i, n)

def insert(heap, value):
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2  # Indeks rodzica

        if heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]  # Zamieniamy miejscami rodzica i nowy element
            i = parent  # Przechodzimy do rodzica
        else:
            break

arr = [2,5,3,4,5,1,3,4,6]