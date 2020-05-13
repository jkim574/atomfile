class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(len(self.items)+1,item)

    def dequeue(self):
        self.items.remove(self.items[0])

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print(self.items)


q = Queue()
print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(5)
q.print_queue()
q.dequeue()
q.print_queue()
q.dequeue()
q.print_queue()
