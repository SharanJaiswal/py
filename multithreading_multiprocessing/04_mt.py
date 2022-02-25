'''
Daemon thread is the thread that runs continuously in the background, provides supports to the non-deamon threads. We can make any thread as a daemon thread. 
But by nature of deamon thread, it should be supportive in nature. 
When last Deamon thread terminates, automatically all deamon thread terminates. We are not required to terminate the deamon thread explicitly.
Ways to create non-deamon thread to deamon thread:  i) setDeamon(True) Method,  ii) deamon=True Property. For Deamon to non-deamon thread, use False in place of True
To check if the thread is deamon thread or not: i) isDeamon() Method -> True|False   ii) deamon Property(same as above) -> True|False
Active non-daemon thread cannot be changed to deamon, and vice-versa. Before using start we are allowed to change the thread status to deamon or non-deamon, not after starting it.
'''


import threading, time

def teacher():
    for i in range(1,11):
        print('Teaching session:', i)
        time.sleep(0.5)
    
def main():
    # Daemon value must be set before the start method is called for that thread. Otherwise, it will throw a runtime error.
    # Initial value of daemon status of the thread is inherited from the thread it is created from.
    # MainThread is not a Daemon thread. Hence, actual normal python code is not a daemon thread.
    # entire python program exits when no alive non-daemon threads are left. Hence when main thread closes, then only THE PYTHON PROGRAM closes since PYTHON is DAEMON.

    main_thread = threading.enumerate()[0]
    print(main_thread)
    print(main_thread.isDaemon())   # MainTread by default is non-Deamon thread. Any Child thread, by default, inherits the deamon nature of its parent at the time when it was created(not necessarily when child was started)

    print()

    t1=threading.Thread(target=teacher)
    print(t1.isDaemon())
    # t1.setDaemon(True)    
    # Above, if t1 is set to deamon, then when non-deamon thread MainThread completed execution, then automatically this t1 deamon thread ends in the middle, just after the execution of last non-deamon thread(which is MainThread here)
    # Otherwise, even after main completes its execution its last"Exam fin" statement, the t1 non-deamon thread will continue to execute.
    print(t1.isDaemon())
    t1.start()
    time.sleep(3)
    # t1.join() # Even if t1 is set to deamon thread, and we are required to let it execute completely, then we wait here to get merged to the parent (MainThread) thread
    print('Exam Finished', threading.current_thread().getName())

    print(threading.enumerate())


if (__name__ == '__main__'):
    main()