class Node:
    '''Creates and represents individual element in the singly/doubly linkedlist'''
    def __init__(self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class linkedList:
    pass

class singleLinkedList:
    def __init__(self):
        ''' head variable points to the start of the linkedlist '''
        self.head=None

    def insert_at_begining(self, data):
        ''' insertion of new node at the begining as head-->new-->existing list '''
        node = Node(data, self.head)        # node created with its next pointing to the current value of head, apparently existing LL. head points to None for first node
        del node.prev       # deleting the previous node reference pointer since its SLL
        self.head = node        # to add this node to the current LL, current head(pointing None) should point to new node.
        return

    def insert_at_end(self, data):
        ''' inserting after the last inserted node. Or, the first node, if the list is empty '''
        if self.head==None:
            node=Node(data)
            del node.prev
            self.head=node
            return
        
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data)
            del node.prev
            itr.next = node
            return

    def insert_val_by_list(self, data_list):
        ''' making LL with its elemnts of list '''
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)
        return

    def printll(self):
        ''' prints the linked list object '''
        if self.head is None:
            print("Linked list is empty")
            return
        # else part
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        llstr = llstr.rstrip("-->")
        print(llstr)
        return

    def get_ll_length(self):
        '''count the number of elemnts in LL'''
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def delete_at_index(self, index):
        ''' deleting element at particular index where indexing startrs from 0 '''
        if index<0 or index>=self.get_ll_length():
            raise Exception("Index out of bound!!!")

        elif index==0:
            self.head = self.head.next

        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def insert_at_index(self, index, data):
        if (index < 0) or (index >= self.get_ll_length()):
            raise Exception("Index out of bound.")

        elif index ==0:
            self.insert_at_begining(data)

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    del node.prev
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def insert_after_value(self, value, data):
        if self.head == None:
            raise Exception("Empty linked list. Value does not exist.")
        
        else:
            itr = self.head
            while itr:
                if itr.data == value:
                    node = Node(data, itr.next)
                    itr.next = node
                    return
                itr = itr.next
            if not itr:
                raise Exception("Value does not exist.")

    def remove_by_value(self, value):
        if self.head == None:
            raise Exception("Empty Linked List.")
        
        elif self.head.data == value:
            self.head = self.head.next

        else:
            itr = self.head
            while itr.next:
                if itr.next.data == value:
                    itr.next = itr.next.next
                    break
                itr = itr.next
            if not itr.next:
                raise Exception("Value not found.")

class doubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data, None, itr)

    def insert_val_by_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)

    def printll(self, rev=False):
        if self.head is None:
            print("Linked List is empty.")

        elif rev == False:
            itr = self.head
            llstr = ''

            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            llstr = llstr.rstrip('->')
            print(llstr)

        elif rev == True:
            itr = self.head
            llstr = ''

            while itr.next:
                itr = itr.next
            
            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.prev
            llstr = llstr.rstrip('->')
            print(llstr)
    
    def get_ll_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def delete_at_index(self, index):
        if (index < 0) or (index >= self.get_ll_length()):
            raise Exception("Index out of Bound.")
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    if itr.next is not None:
                        itr.next.prev = itr
                    break
                count += 1
                itr = itr.next

    def insert_at_index(self, index, data):
        if (index < 0) or (index >= self.get_ll_length()):
            raise Exception("Index out of bound")

        elif index == 0:
            self.insert_at_begining(data)
        
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next, itr)
                    itr.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def insert_after_value(self, value, data):
        if self.get_ll_length() == 0:
            raise Exception("Empty linked list. Value cannot be found")
        
        else:
            itr = self.head
            while itr:
                if itr.data == value:
                    node = Node(data, itr.next, itr)
                    itr.next.prev = node
                    itr.next = node
                    return
                itr = itr.next
            if not itr:
                raise Exception("Value does not exist.")

    def remove_by_value(self, value):
        if self.head == None:
            raise Exception("Empty Linked List.")
        
        elif self.head.data == value:
            self.head = self.head.next
            self.head.prev = None

        else:
            itr = self.head
            while itr.next:
                if itr.next.data == value:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    break
                itr = itr.next
            if not itr.next:
                raise Exception("Value not found.")


if __name__ == '__main__':
    sll = singleLinkedList()       # linkedlist object created

    sll.insert_at_begining(5)
    sll.insert_at_begining(6)
    sll.insert_at_begining(8)
    sll.printll()
    

    sll.insert_at_end('c')
    sll.insert_at_end('v')
    sll.insert_at_end('b')
    sll.insert_at_end('a')
    sll.printll()


    sll.insert_val_by_list([1,2,3,4,'fg', 45,56,345,3])
    sll.printll()

    print("Elements in LL is:", sll.get_ll_length())

    sll.delete_at_index(3)
    sll.printll()

    sll.insert_at_index(0, "figs1")
    sll.insert_at_index(0, "figs2")
    sll.insert_at_index(5, "on nom")
    sll.printll()

    sll.insert_after_value(3, 'sharan')
    sll.printll()

    sll.remove_by_value('figs1')
    sll.printll()
    sll.remove_by_value('figs2')
    sll.printll()


if __name__ == '__main__':
    dll = doubleLinkedList()

    dll.insert_at_begining(1)
    dll.insert_at_begining("OOOOOOooooo.......")
    dll.insert_at_begining("jaiswal")
    dll.printll(True)
    dll.printll()

    dll.insert_at_end(343)
    dll.insert_at_end(complex(7j))
    dll.insert_at_end(complex(7))
    dll.printll()

    dll.insert_val_by_list((('qwerty'), ('asdfgh'), ('zxcvbn'), ('qazws'), ('rfvtgbyhn')))
    dll.printll()

    print("total current number of nodes: ", dll.get_ll_length())

    dll.delete_at_index(4)
    dll.printll()
    dll.delete_at_index(2)
    dll.printll()

    dll.insert_at_index(2, 'tutul')
    dll.printll()

    dll.insert_after_value('tutul', 'dinner')
    dll.printll()

    dll.remove_by_value('dinner')
    dll.printll()
    