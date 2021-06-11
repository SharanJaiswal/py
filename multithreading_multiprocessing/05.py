import threading

def first_func():
    global x
    global lock

    lock.acquire()
    try:
        while(x < 300):
            x += 1

        if x == 300:
            print(x)
    finally:
        lock.release()
        #pass
    
def second_func():
    global x
    global lock

    print('sharan jaiswal')
    lock.acquire()
    try:
        x = 450
        while(x < 600):
            x += 1
        
        print(x)
    finally:
        lock.release()

def main():
    global x, lock  # lock has to be global so that it can be accessed from different thread targets
    ''' locks dont allow one thread to start dealing with one shared resource before another thread finished dealing with that one shared resource'''
    '''similar to join, but here threads are started simultaneously, but they aren't allowed to share same resources at a time, until it is released by the current thread'''
    x = 0

    lock = threading.Lock() # defining lock variable

    first_thread = threading.Thread(target = first_func, name = 'first thread function')
    first_thread.start()

    second_thread = threading.Thread(target = second_func, name = 'second thread function')
    second_thread.start()

    print(threading.enumerate())


if (__name__ == '__main__'):
    main()