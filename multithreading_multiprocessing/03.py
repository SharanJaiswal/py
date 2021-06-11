import threading

def first_func():
    global x

    while(x < 300):
        x += 1

    if x == 300:
        print(x)
    
def second_func():
    global x
    
    x = 450
    while(x < 600):
        x += 1
    
    print(x)

def main():
    global x
    x = 0

    first_thread = threading.Thread(target = first_func, name = 'first thread function')
    print(first_thread.ident)
    first_thread.start()
    print(first_thread.ident)
    #first_thread.join()
    print(first_thread.ident)

    second_thread = threading.Thread(target = second_func, name = 'second thread function')
    print(first_thread.ident)
    print(second_thread.ident)
    second_thread.start()
    print(first_thread.ident)
    print(second_thread.ident)
    print(first_thread.ident)
    print(second_thread.ident)
    print(first_thread.ident)
    print(second_thread.ident)
    print(first_thread.ident)
    print(second_thread.ident)

    print(threading.enumerate())

    ''' Every thread has its own ident, which is initialized after when it is defined, not necessarily for it to start.
        Even MainThread has its ident. Thread after its completion, merges into parent thread. Hence it attains ident similar to its parent ident, after its merging with parent ident.
        So, whwenver two threads have same ident, then at that point of time, they are merged, i.e., they are not individual.'''


if (__name__ == '__main__'):
    main()