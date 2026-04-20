import heapq
class PriorityQueue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (priority, value))

    def dequeue(self):
        if not self.queue:
            raise IndexError("Queue is empty")
        priority, value = heapq.heappop(self.queue)
        return f"delete val: {value}; priority {priority}"

heap=PriorityQueue()
heap.enqueue("task1", 2)
heap.enqueue("task2", 1)
heap.enqueue("task3", 4)
heap.enqueue("task4", 3)
print(heap.queue)
print(heap.dequeue())
print(heap.queue)


