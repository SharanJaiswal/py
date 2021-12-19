import threading

def first_func():
    global x

    while(x < 300):
        x += 1

    print(threading.current_thread())
    if x == 300:
        print(x)
    
def second_func():
    global x
    
    x = 450
    while(x < 600):
        x += 1
    
    print(threading.current_thread())
    print(x)

def main():
    global x
    x = 0

    first_thread = threading.Thread(target = first_func, name = 'first thread function')
    first_thread.start()
    #first_thread.join()
    ''' mian thread will wait for the child threads to get completed before completing its execution.
    Its like, where ever threrad's join will be invoked, the control flow of execution wont execute its parent thread, and parent thread will wait for that child thread to get completed.
    Then only, the next command/instruction of parent thread will execute.'''

    second_thread = threading.Thread(target = second_func, name = 'second thread function')
    second_thread.start()

    print(threading.enumerate())
    print(threading.current_thread())


if (__name__ == '__main__'):
    main()