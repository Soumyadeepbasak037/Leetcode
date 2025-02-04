class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            return

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            return

    # def insert_at_index(self, index, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         print("Are you retarded?")

    def print_list(self):

        if self.head is None:
            print("No head")
        else:
            temp = self.head
            while (temp):
                print(temp.data, end="->")
                temp = temp.next

    def insert_at_index(self, index, data):
        if self.head is None:
            print("Are you retarded?")
        else:
            new_node = Node(data)
            curr = self.head
            counter = 0
            while counter != index-1:
                temp = curr
                # curr = curr.next
                temp.next = new_node
                new_node.next = curr.next
                print(temp.data, " ", curr.data)
                counter += 1


ll1 = linked_list()
ll2 = linked_list()

ll1.insert_at_end(1)
ll1.insert_at_end(2)
ll1.insert_at_end(4)

ll2.insert_at_end(1)
ll2.insert_at_end(3)
ll2.insert_at_end(4)


ll1.print_list()
print(" ")
ll2.print_list()
print(" ")


ans_ll = linked_list()


def ll_to_arr(head: Node, arr):
    curr_node = head
    while (curr_node):
        arr.append(curr_node.data)
        curr_node = curr_node.next


arr = []

ll_to_arr(ll1.head, arr)
ll_to_arr(ll2.head, arr)
arr.sort()
print(arr)

for i in arr:
    ans_ll.insert_at_end(i)
ans_ll.print_list()

print(' ')
ll2.insert_at_index(2, 10)
