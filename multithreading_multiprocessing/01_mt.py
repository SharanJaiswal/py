import threading
import time

def do_this():
    print("This is our thread!")

def main():

    our_thread = threading.Thread(target=do_this)   # created thread and provided it target that this thread will do this target when initialized.
    our_thread.start()  # this will start the thread.
    # time.sleep(0.1)
    print(our_thread.is_alive())

    print(threading.active_count()) # count of thread objects that are alive. Actually it returns the length of threading.enumerate()
    print(threading.enumerate())    # outputs the list of thread, child thread name, start epoc of that thread
    print(threading.current_thread())   
    print(threading.current_thread().getName())   

if (__name__ == '__main__'):
    main()