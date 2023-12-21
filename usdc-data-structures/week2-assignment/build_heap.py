# python3
import math

def sift_down(heap, idx, swaps, size):
    min_index = idx
    left = get_left_child(idx)
    if left <= size and heap[left] < heap[min_index]:
        min_index = left
    right = get_right_child(idx)
    if right <= size and heap[right] < heap[min_index]:
        min_index = right
    if idx != min_index:
        swaps.append((idx, min_index))
        heap[idx], heap[min_index] = heap[min_index], heap[idx]
        sift_down(heap, min_index, swaps, size)

def get_left_child(idx):
    return 2 * idx + 1

def get_right_child(idx):
    return 2 * idx + 2

def build_heap(data):
    swaps = []
    num_elements = len(data)
    for i in range((num_elements//2) -1 , -1 , -1):
        sift_down(data, i, swaps, len(data) - 1)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
