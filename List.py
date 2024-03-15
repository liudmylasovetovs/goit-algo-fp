class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node


    def merge_sorted_lists(self, list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.sorted_insert(Node(current1.data))
                current1 = current1.next
            else:
                merged_list.sorted_insert(Node(current2.data))
                current2 = current2.next

        while current1 is not None:
            merged_list.sorted_insert(Node(current1.data))
            current1 = current1.next

        while current2 is not None:
            merged_list.sorted_insert(Node(current2.data))
            current2 = current2.next

        return merged_list

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Приклад використання:

# Створення списку 1: 1 -> 3 -> 5
list1 = LinkedList()
list1.sorted_insert(Node(1))
list1.sorted_insert(Node(3))
list1.sorted_insert(Node(5))

# Створення списку 2: 2 -> 4 -> 6
list2 = LinkedList()
list2.sorted_insert(Node(2))
list2.sorted_insert(Node(4))
list2.sorted_insert(Node(6))

print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

# Об'єднання відсортованих списків
merged_list = LinkedList().merge_sorted_lists(list1, list2)
print("Merged List:")
merged_list.print_list()

# Реверсування списку
merged_list.reverse()
print("Reversed Merged List:")
merged_list.print_list()
