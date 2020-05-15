


class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    #function to get data of particular node
    def get_data(self):
        return self.data

    #functino to get next node
    def get_next(self):
        return self.next

    #function to set data
    def set_data(self, data):
        self.data = data

    #function to set next node
    def set_next(self, next):
        self.next = next







class LinkedList(object):
    #defining the head of the linked list
    def __init__(self, head = None):
        self.head = head

    #printing the data in the linked list
    def print_linkedlist(self):
        curr = self.head
        while(curr != None):
            print(curr.get_data())
            curr = curr.get_next()

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            curr.next = node

    def size(self):
        curr = self.head
        count = 0
        while(curr != None):
            curr = curr.get_next()
            count += 1
        return count


    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def is_empty(self):
        return self.head == None


if __name__ == '__main__':
    test = LinkedList()
    test.append(Node(3))
    test.append(Node(30))
    test.append(Node(1))
    test.append(Node(5))
    # test.append(Node(9))
    # test.append(Node(10))
    test.print_linkedlist()
    print(test.is_empty())
    print("size is:", test.size())
    test.remove(3)
    test.remove(1)
    test.print_linkedlist()
