class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueue {item} to the queue.")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"dequeued {item} from the queue.")
        return item
    def peek(self):
        if self.is_empty():
            print("queue is empty.Cannot peek.")
            return None 
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def display(self):
        if self.is_empty():
            print("queue is empty.")
        else:
            print("Queue:",self.queue)
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("front element:",queue.peek())
queue.dequeue()
queue.display()
print("queue size:", queue.size())