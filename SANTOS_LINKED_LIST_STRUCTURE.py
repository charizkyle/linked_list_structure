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

# ➤ MAIN EXECUTION
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("\nLINKED LIST:")
sushi_preparation.print_list()

# remove at beginning
removed = sushi_preparation.remove_beginning()
print(f"\nREMOVED AT BEGINNING ('{removed}'):")
sushi_preparation.print_list()