class hashTable:
    '''without collision. Even if present, key value will be updted with the collided value'''
    def __init__(self, size):
        self.max=size
        self.table = [None for I in range(self.max)]
    
    def get_hash(self, key):
        key = str(key)
        h=0
        for char in key:
            h += ord(char)
        return h%self.max

    #def add(self, key, value):
    def __setitem__(self, key, value):
        key = str(key)
        h = self.get_hash(key)
        self.table[h] = value

    #def get_hash_value(self, key):
    def __getitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        return self.table[h]

    def __delitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        self.table[h] = None

class hashTableChaining:
    '''this hash table class handles collision by the method of chaining.
        same key value will be overrided, but same hash value will be chanined.'''
    def __init__(self, size):
        self.max = size
        self.table = [[] for i in range(self.max)]

    def get_hash(self, key):
        key = str(key)
        h = 0
        for char in key:
            h += ord(char)
        return h%self.max
    
    def __getitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        for element in self.table[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value): # storing it in the form of (key, value) in the sublist
        key = str(key)
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.table[h]):   # updating the value of key in sublist, if new key is alredy present for its given hash
            if len(element)==2 and element[0]==key:
                self.table[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.table[h].append((key, value))

    def __delitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        for idx,element in enumerate(self.table[h]):
            if element[0] == key:
                del self.table[h][idx]

class hashTableLinearProbing:
    def __init__(self, size):
        self.max = size
        self.table = [None for i in range(self.max)]
    
    def get_hash(self, key):
        key = str(key)
        h = 0
        for char in key:
            h += ord(char)
        return h%self.max

    def __setitem__(self, key, value):
        key = str(key)
        h = self.get_hash(key)
        start_idx = h
        flag = 0
        while True:
            if flag != 0 and h == start_idx:
                print("Table is full.")
                break
            
            if self.table[h] != None:
                if self.table[h][0] == key:
                    self.table[h] = (key, value)
                    return
                flag = 1
                h += 1
                h %= self.max
                continue
            
            if self.table[h] == None:
                self.table[h] = (key, value)
                return

    def __getitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        start_idx = h
        flag =0
        while True:
            if flag != 0 and h == start_idx:
                print("No entry found.")
                break

            if self.table[h][0] != key:
                flag = 1
                h += 1
                h %= self.max
                continue

            if self.table[h] == key:
                return self.table[h][1]

    def __delitem__(self, key):
        key = str(key)
        h = self.get_hash(key)
        start_idx = h
        flag = 0
        while True:
            if flag != 0 and h == start_idx:
                print("Item not found.")
                break

            if self.table[h][0] != key:
                flag = 1
                h += 1
                h %= self.max
                continue

            if self.table[h][key] == key:
                del self.table[h]
                return

if __name__ != '__main__':
    t = hashTable(10)
    print(t['sharan'])      # calls __getitem__
    t['sharan'] = 'JaiswaL'     # callls __setitem__
    print(t['sharan'])      # calls __getitem__
    print(t.table)
    del t['sharan']     # calls __delitem__
    print(t.table)

if __name__ != '__main__':
    t = hashTableChaining(10)

    print(t.table)
    t['march 6'] = 120
    t['march 6'] = 78
    print(t.table)
    print(t['march 6'])
    t['march 8'] = 67
    t['march 9'] = 4
    t['march 17'] = 459

    print(t['march 6'])
    print(t['march 17'])

    print(t.table)

    del t['march 17']
    print(t.table)
    print(t['march 17'])

if __name__ != '__main__':
    t = hashTableLinearProbing(5)
    t[5] = 'five'
    t[5] = 'five'
    t[1] = 'one'
    t[5] = 'FIVE'
    t[2] = 'second'
    t['10'] = 'five5'
    print(t.table)