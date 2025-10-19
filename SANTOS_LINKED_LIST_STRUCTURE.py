class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        if not current_node:
            print("X")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("X")

    # remove at beginning
    def remove_beginning(self):
        if self.head:
            removed = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed
        return None
    
        # remove at end
    def remove_at_end(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            removed = self.head.data
            self.head = None
            self.tail = None
            return removed

        current = self.head
        while current.next != self.tail:
            current = current.next
        
        removed = self.tail.data
        current.next = None
        self.tail = current
        return removed
    
    # remove_at(self, data)
    def remove_at(self, data):
        if self.head is None:
            return None
        
        if self.head.data == data:  # If it's the head
            return self.remove_beginning()

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:  # Found the node
            removed = current.next.data
            if current.next == self.tail:  # If it's the tail
                self.tail = current
            current.next = current.next.next
            return removed
        return None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")

# ➤ MAIN EXECUTION
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("\nSUSHI PREP LINKED LIST:")
sushi_preparation.print_list()

# remove at beginning
removed = sushi_preparation.remove_beginning()
print(f"\nREMOVED AT BEGINNING ('{removed}'):")
sushi_preparation.print_list()

# remove at end
removed = sushi_preparation.remove_at_end()
print(f"\nREMOVED AT END ('{removed}'):")
sushi_preparation.display()

# remove at specific data
removed = sushi_preparation.remove_at("prepare")
print(f"\nREMOVED ('{removed}'):")
sushi_preparation.display()