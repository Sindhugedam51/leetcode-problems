import heapq
priority_queue = []
heapq.heappush(priority_queue, (2, "Task B"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (3, "Task C"))
print("Priority Queue:", priority_queue)
while priority_queue:
    print("Dequeued:", heapq.heappop(priority_queue))
    