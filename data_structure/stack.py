class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
#        print(self.items)
        return len(self.items) == 0

    def print_stack(self):
        print(self.items)


s = stack()

s.print_stack()
print(s.is_empty())
s.push(4)
s.push(5)
s.push(10)
print(s.size())
print(s.is_empty())
print(s.peek())
s.print_stack()
