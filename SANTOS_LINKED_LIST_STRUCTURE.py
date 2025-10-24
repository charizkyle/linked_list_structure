class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print(" -> X\n")

    # Remove at beginning
    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # Remove at end
    def remove_at_end(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    # Remove a specific node by data
    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                return removed_data
            current = current.next
        return None


# ➤ MAIN EXECUTION
sushi_preparation = LinkedList()
steps = ["prepare", "cook rice", "slice ingredients", "roll sushi", "serve"]
for step in steps:
    sushi_preparation.append(step)

print("\nHOW TO MAKE A SUSHI 🍣 (LINKED LIST):")
sushi_preparation.display()

# Remove at beginning
removed = sushi_preparation.remove_beginning()
print(f"\nREMOVED AT BEGINNING ('{removed}'):")
sushi_preparation.display()

# Remove at end
removed = sushi_preparation.remove_at_end()
print(f"\nREMOVED AT END ('{removed}'):")
sushi_preparation.display()

# User input for random removal (loops until valid)
while True:
    user_input = input("Enter a step to remove: ")
    removed_at = sushi_preparation.remove_at(user_input)

    if removed_at:
        print(f"\nREMOVED AT ('{removed_at}'):")
        sushi_preparation.display()
        break  # Stop the loop once a valid removal happens
    else:
        print("X")  # Print X if not found, then ask again

# Final Linked List after removals
print("\nFINAL 🍣SUSHI PREPARATION🍣 LINKED LIST AFTER REMOVALS:")
sushi_preparation.display()