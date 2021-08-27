# Sharing data between two processes using multiprocessing.Queue in python
# It is different than queue Data Structures from queue.Queue(), which lives in in-process memory, and is used to share data between threads
# While multiprocessing.Queue() resides in shared memory and is used to share data between processes
# multiprocessing.Queue() has its own methods

import multiprocessing

def calc_square(numbers, q):
    for num in numbers:
        q.put(num * num)
    print(q)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))

    p.start()
    p.join()

    print(q)
    print()

    while q.empty() is False:
        print(q.get())