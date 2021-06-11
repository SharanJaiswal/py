# list; collections.deque; queue.LifoQueue
#sp = []
#sp.insert(0, 25)
#sp.insert(0, 23)
#sp.insert(0, 67)
#print(sp)
#sp.pop()
#sp.pop()
#sp.pop()
#print(sp)
#sp.pop()

from collections import deque
import time, threading

class Queue:
    def __init__(self, size = None):
        self.max = size
        self.buffer = deque([], self.max)
    
    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.max

    def enqueue(self, value):
        if not self.is_full():
            self.buffer.appendleft(value)
        else:
            print('Buffer is full. Pop some items.')
   
    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()
        else:
            print('Buffer is already empty. Nothing to pop out.')

    def size(self):
        return len(self.buffer)

    def peek(self):
        return self.buffer[-1]

if __name__ != '__main__':
    que = Queue(5)
    print(que.size())
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    print(que.buffer)
    print(que.size())
    que.enqueue(5)
    print(que.buffer)
    que.enqueue(6)
    print(que.size())
    print(que.buffer)

if __name__ != '__main__':

    def place_order(que, orders):
        for order in orders:
            print("Placing order for:",order)
            que.enqueue(order)
            time.sleep(2)

    def serve_order(que):
        while True:
            print("Now serving: ", que.dequeue())
            time.sleep(5)

    que = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target = place_order, args = (que, orders), name = 'place')
    t2 = threading.Thread(target = serve_order, args = (que,), name = 'serve')

    t1.start()
    time.sleep(1)
    t2.start()

if __name__ != '__main__':
    que = Queue()
    que.enqueue("1")
    for i in range(10):
        top = que.peek()
        que.enqueue(top + "0")
        que.enqueue(top + "1")
        print(que.dequeue())
