# Concept of locks

import multiprocessing
import time

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # Sandwiching critical section of code, where shared resources needs to be protected, between the lock
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # Sandwiching critical section of code, where shared resources needs to be protected, between the lock
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)

    lock = multiprocessing.Lock()

    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)
    # We are expecting the 200 as an answer because equal number of deposits and with same amount has been occured, but this does not occured
    # if locks are not present then this will right value from the shared variable, but the execution deviates it from the expected value
    # It happens because, by the time LHS of one process gets executed, another process gets executed. This 