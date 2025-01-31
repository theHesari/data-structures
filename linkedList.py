class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = self.head  
            self.head.prev = self.head  
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head 
            self.head.prev = node  
            self.tail = node
        self.length += 1

    def remove(self, value):
        if self.head is None:  
            raise ValueError("List is empty")

        current = self.head
        while current is not None:
            if current.value == value:
                if current == self.head:
                    if self.head.next == self.head:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = current.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else: 
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1
                return f"Node {value} removed"
            current = current.next

        raise ValueError(f"Value {value} not found in the list")
    
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # Using Floyd’s Cycle Detection Algorithm
    def detect_loop(self):
        slow = self.head
        fast = self.head
        hasLoop = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasLoop = True
                break
        print("Loop detected:", hasLoop)

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = self.head  
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head 
        self.length += 1

    def remove(self, value):
        if self.head is None: 
            raise ValueError("List is empty")

        current = self.head
        if current.value == value:  
            if current.next == self.head:  
                self.head = None
            else:
                self.head = current.next
                self.tail.next = self.head
            self.length -= 1
            return f"Node {value} removed"
        
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
            if current.value == value:
                prev.next = current.next
                self.length -= 1
                return f"Node {value} removed"

        raise ValueError(f"Value {value} not found in the list")
    
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def detect_loop(self):
        slow = self.head
        fast = self.head
        hasLoop = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasLoop = True
                break
        print("Loop detected:", hasLoop)

def doubly_circular_linked_list():
    dll = DoublyCircularLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.print_list()
    dll.remove(2)
    dll.print_list()
    dll.detect_loop()

def singly_circular_linked_list():
    sll = SinglyCircularLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.print_list()
    sll.remove(2)
    sll.remove(3)
    sll.print_list()
    sll.detect_loop()


if __name__ == "__main__":
    doubly_circular_linked_list()
    singly_circular_linked_list()
