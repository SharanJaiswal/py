''' tree can have * children. every node of tree is capable of being a root of its own tree.
Hence, recursively, every node can be a tree with itself being a root node of that sub-tree'''
if __name__ != '__main__':
    class TreeNode: # an individual node
        def __init__(self, data):
            self.data = data
            self.children = []
            self.parent = None

        def add_child(self, child): # you can check also here for duplicacy
            child.parent = self
            self.children.append(child)

        def get_level(self):
            count = 0
            p = self.parent
            while p:
                count += 1
                p = p.parent
            return count

        def print_tree(self):
            level = self.get_level()
            spaces = ' ' * level * 3
            prefix = spaces + '|--' if self.parent else ''
            print(prefix, self.data)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree()

    def build_product_tree():
        root = TreeNode('Electronics')

        laptop = TreeNode('Laptop')
        laptop.add_child(TreeNode('Mac'))
        laptop.add_child(TreeNode('Surface'))
        laptop.add_child(TreeNode('Thinkpad'))

        cellphone  = TreeNode('Cell Phone')
        cellphone.add_child(TreeNode('iPhone'))
        cellphone.add_child(TreeNode('Google Pixel'))
        cellphone.add_child(TreeNode('Vivo'))

        tv = TreeNode('TV')
        tv.add_child(TreeNode('Samsung'))
        tv.add_child(TreeNode('LG'))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        return root

    root = build_product_tree()
    print(root.print_tree())

if __name__ != '__main__':
    class TreeNode:
        def __init__(self, value):
            self.post = value[0]
            self.name = value[1]
            self.parent = None
            self.children = []

        def add_child(self, child):
            self.children.append(child)
            child.parent = self

        def get_level(self):
            count = 0
            p = self.parent
            while p:
                count += 1
                p = p.parent
            return count

        def print_tree(self, type):
            level = self.get_level()
            spaces = ' ' * level * 2
            prefix = spaces + '|----' if self.parent else ''
            if type == 'both':
                print(prefix, self.name, '('+self.post+')')
            if type == 'name':
                print(prefix, self.name)
            if type == 'designation':
                print(prefix, self.post)
            if self.children:
                for child in self.children:
                    child.print_tree(type)

    ceo = TreeNode(['CEO', 'Nilipul'])
    cto = TreeNode(['CTO', 'Chinmay'])
    hr_head = TreeNode(['HR Head', 'Gels'])
    infra_head = TreeNode(['Infrastructure Head', 'Vishwa'])
    ceo.add_child(cto)
    ceo.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(TreeNode(['Application Head', 'Aaamir']))
    infra_head.add_child(TreeNode(['Cloud Manager', 'Dhaval']))
    infra_head.add_child(TreeNode(['App Manager', 'Abhijit']))
    hr_head.add_child(TreeNode(['Recruitment Manager', 'Peter']))
    hr_head.add_child(TreeNode(['Policy Manager', 'Waqas']))

    ceo.print_tree('name')
    ceo.print_tree('designation')
    ceo.print_tree('both')

if __name__ != '__main__':
    class Place:
        def __init__(self, value):
            self.value = value
            self.children = []
            self.parent = None

        def add_child(self, child):
            child.parent = self
            self.children.append(child)
        
        def get_level(self):
            count = 0
            p = self.parent
            while p:
                count += 1
                p = p.parent
            return count

        def print_tree(self, hier):
            level = self.get_level()
            if hier >= level:
                spaces = ' ' * level * 2
                prefix = spaces + '|---' if self.parent else ''
                print(prefix, self.value)
                for child in self.children:
                    child.print_tree(hier)            


    whole = Place('Global')
    ind = Place('India')
    whole.add_child(ind)
    guj = Place('Gujarat')
    guj.add_child(Place('Ahmedabad'))
    guj.add_child(Place('Baroda'))
    kar = Place('Karnataka')
    kar.add_child(Place('Bengaluru'))
    kar.add_child(Place('Mysore'))
    ind.add_child(guj)
    ind.add_child(kar)
    usa = Place('USA')
    whole.add_child(usa)
    new_jer = Place('New Jersey')
    cal = Place('California')
    usa.add_child(new_jer)
    usa.add_child(cal)
    new_jer.add_child(Place('Princeton'))
    new_jer.add_child(Place('Trenton'))
    cal.add_child(Place('San Francisco'))
    cal.add_child(Place('Mountain View'))
    cal.add_child(Place('Palo Alto'))

    whole.print_tree(3)

