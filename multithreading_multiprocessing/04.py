import threading

def first_func():
    global x

    while(x < 300):
        x += 1

    if x == 300:
        print(x)
    
def main():
    global x
    x = 0

    # Daemon value must be set before the start is called for that thread. Otherwise, it will throw a runtime error.
    # Initial value of the thread is inherited from the thread it is created from.
    # MainThread is not a Daemon thread. Hence, actual normal python code is not a daemon thread.
    # entire python program exists when no alive non-daemon threads are left. Hence when main thread closes, then only THE PYTHON PROGRAM closes.

    main_thread = threading.enumerate()[0]
    print(main_thread)
    print(main_thread.isDaemon())

    print()

    first_thread = threading.Thread(target = first_func, name = 'first thread function')
    #first_thread.setDaemon(True)
    first_thread.start()
    print(first_thread.isDaemon())

    print(threading.enumerate())


if (__name__ == '__main__'):
    main()