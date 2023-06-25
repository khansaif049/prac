class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.is_empty():
            print("Linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

def process_linked_list(l1,l2):
    sub_val = str(int(get_str_val(l1)) + int(get_str_val(l2)))[::-1]
    s = lst2link(sub_val)
    return s


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next



def get_str_val(ll):
    str_of_ll = ""
    itr = ll.head
    while itr:
        str_of_ll += str(itr.data)
        itr = itr.next
    print(str_of_ll[::-1],"str_of_ll")
    return str_of_ll[::-1]


my_list = LinkedList()
my_list.insert_at_head(4)
my_list.insert_at_head(2)
my_list.insert_at_tail(3)
my_list.display()

my_list_2 = LinkedList()
my_list_2.insert_at_head(6)
my_list_2.insert_at_head(5)
my_list_2.insert_at_tail(4)

# Pass the linked list to the function
process_linked_list(my_list,my_list_2)