


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
        self.curr = curr






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

    # def append_index(self, previous_node, node):
    #     if (previous_node is None):
    #         print("Previous Node doens't exist")
    #     else:
    #         curr = curr.next

    def len("")


    def is_empty(self):
        if len(self.head) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    test = LinkedList()
    test.head = Node(3)
    test.append(Node(1))
    test.append(Node(5))
    # test.append(Node(9))
    # test.append(Node(10))
    test.print_linkedlist()
    test.is_empty()



# public void print() {
#         Node<T> curr = this.head;
#        	while (curr != null) {
# 	    System.out.println(curr.getData());
# 	    curr = curr.getNext();
# 	}
#     }

#         class linkedListNode:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.nextNode = nextNode


# class linkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def insert(self, value):
#         node = linkedListNode(value)
#         if self.head is None:
#             self.head = node
#             return

#         currentNode = self.head
#         while True:
#             if currentNode.nextNode is None:
#                 currentNode.nextNode = node
#                 break
#             currentNode = currentNode.nextNode

#     def printLinkedList(self):
#         currentNode = self.head
#         while currentNode is not None:
#             print currentNode.value, "->",
#             currentNode = currentNode.nextNode
#         print "None"




# ll = linkedList()
# ll.printLinkedList()
# ll.insert("3")
# ll.printLinkedList()
# ll.insert("44")
# ll.printLinkedList()
# ll.insert("55")
# ll.printLinkedList()




# Nodes
# 1. Value - anything strings, integers, objects
# 2. The Next Node


# class linkedListNode:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.nextNode = nextNode


# def insertNode(head, valuetoInsert):
#     curr = curr.next()
#     head
# #     currentNode = head
# #     while currentNode is not None:
#         if currentNode.nextNode is None:
#             currentNode.nextNode = linkedListNode(valuetoInsert)
#             return head
#         currentNode = currentNode.nextNode

#
