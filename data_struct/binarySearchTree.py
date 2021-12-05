'''left sub tree has all elements less than its parent node.
Right sub tree has all the element greater than parent node.
Ideally, all data must be unique throughout the tree.'''

class BST:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def add_child(self, value):
        if value == self.data:
            return
        
        elif value < self.data:
            # value must be shifted to left sub-tree

            if self.left:   # if left node of current node in inspection has already some value, then...
                self.left.add_child(value)

            else:   # if left node of current node in inspection has no value, then put this value at this place.
                self.left = BST(value)

        else:
            # value must be shifted to right sub-tree
            if self.right:
                self.right.add_child(value)
            
            else:
                self.right = BST(value)

    # in|pre|post-order depends on weather root of tree should apper on middle|atfirst|at_last of the child nodes
    def inorder(self):
        if not self.data:
            return
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self):
        if not self.data:
            return
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if not self.data:
            return
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def search(self, value):
        if self is None or self.data == None:   # if current node in inspection, doesn't even exist (empty tree in consideration) or, has no data
            print('No value present with value', value)

        elif value == self.data:  # if data found is current node in inspection
            return self
        
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return None

        else:
            if self.right:
                return self.right.search(value)
            else:
                return None

    def find_min(self):
        ''' min value in the current tree in inspection is the leftmost value in the tree'''
        if self is None or self.data == None:
            return False
        elif self.left == None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        '''maximum value is the right most node data in the current tree in consideration'''
        if self is None or self.data == None:
            return False
        elif self.right == None:
            return self.data
        else:
            return self.right.find_max()

    def del_node(self, value):
        '''In actual sense, two nodes gets deleted|updated. The one which is requested, & the one which acts as the filler for deleted node'''
        node_pos = self.search(value)   # confirm weather node to be deleted even exists or not
        if node_pos == None:    # if no node is present with data equals to value
            print('Node not present with value', value)
        else:   # if node to be deleted is found with data equals to value, 4 cases arises. node in current inspection has {NO CHILD}|[{ONLY|BOTH}{[LEFT|RIGHT]}CHILD]
            if node_pos.left is None and node_pos.right is None:#if no child present, simply, current node data = None. Later by garbage collection, it'll be removed
                node_pos.data = None
                return node_pos
            elif node_pos.left is None: # If only right child exist, then min of right sub tree should be this node data, ie, node will be same but current data will be updated by min data of right sub-tree.
                filler_side = node_pos.right    # Later, that leftmost min from RST should be deleted
                filler_value = filler_side.find_min()   # The updated RST should be the new RST of current updated node
            elif node_pos.right is None:    # same as above, but just interchange the min-->max & left<--right
                filler_side = node_pos.left
                filler_value = filler_side.find_max()
            else:   # if both child is present, then it is based on business logic/requirements. Choose any one subtree and perform the operation as either of above two
                filler_side = node_pos.right
                filler_value = filler_side.find_min()
            node_pos.data = filler_value    # updaing current data with the sub-tree LEFT|RIGHT-most data
            filler_side = filler_side.del_node(filler_value)    # update the apparently deleted node subtree, with the new subtree where LEFT|RIGHT-most node is removed

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    root = BST(numbers[0])

    for i in range(1, len(numbers)):
        root.add_child(numbers[i])

    root.inorder()
    print("")
    print(root.find_max())
    print(root.find_min())
    print("")
    root.del_node(20)
    root.inorder()
