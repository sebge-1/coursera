# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, worker_index, next_free_time = 0):
        entry = (worker_index, next_free_time)
        self.heap.append(entry)
        self._heapify_up()
    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty priority queue")
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down()
            return min
        else:
            return self.heap.pop()
    def _heapify_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            # if next_free_time is strictly less, always swap
            if self.heap[current_index][1] < self.heap[parent_index][1]:
                self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index],
                current_index = parent_index
            # if next_free_time is tied pick lower index
            elif self.heap[current_index][0] < self.heap[parent_index][0] and self.heap[current_index][1] == self.heap[parent_index][1]:
                self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index],
                current_index = parent_index
            else:
                break
    def _heapify_down(self):
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest = current_index
            if left_child_index < len(self.heap) and self.heap[left_child_index][1] < self.heap[smallest][1]:
                smallest = left_child_index
            elif left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0] and self.heap[left_child_index][1] == self.heap[smallest][1]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index][1] < self.heap[smallest][1]:
                smallest = right_child_index
            elif right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0] and self.heap[right_child_index][1] == self.heap[smallest][1]:
                smallest = right_child_index
            if smallest != current_index:
                self.heap[current_index], self.heap[smallest] = self.heap[smallest], self.heap[current_index]   
                current_index = smallest
            else:
                break
    def is_empty(self):
        return not bool(self.heap)

def assign_jobs(n_workers, jobs):
    worker_queue = PriorityQueue()
    for i in range(n_workers):
        worker_queue.push(i)
    result = []
    
    for job in jobs:
        next_worker = worker_queue.pop()
        result.append(AssignedJob(next_worker[0], next_worker[1]))
        next_worker = (next_worker[0], next_worker[1] + job)
        worker_queue.push(next_worker[0], next_worker[1])
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
