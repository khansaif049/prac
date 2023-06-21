class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
    
    def adding_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def print_ll(self):
        print('callled')
        itr = self.head
        llstr = " "
        suffix = "-->"
        while itr:
            if itr.next:
                llstr += str(itr.data) + suffix
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)

    def get_len(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        print(count)

    def insert_at_end(self,data):
        itr = self.head 
        while itr:
            print(itr.next,"ifnirnf")
            if itr.next:
                pass
            else:
                node = Node(data,None)
                itr.next = node
                break
            itr = itr.next

    def insert_at_ind(self,index,data):
        if index == 0:
            node = Node(data,self.head)
            self.head = node

        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == index :
                node = Node(data,itr.next)
                itr.next = node
                break
            else:
                pass
            itr = itr.next

    def remove_at(self,index):
        count = 0
        itr = self.head

        while itr:
            count += 1
            if index == count+1:
                itr.next = itr.next.next
                break
            else:
                pass
            itr = itr.next



if __name__ == '__main__':
    ll = linked_list()
    ll.adding_at_beg(10)
    ll.adding_at_beg(15)
    ll.adding_at_beg(150)
    ll.adding_at_beg(25)
    ll.insert_at_end(29)
    ll.insert_at_end(34)
    ll.insert_at_ind(1,18)
    ll.print_ll()
    ll.remove_at(2)
    ll.print_ll()
    ll.get_len()