import threading, time, random

def myFunc(n):
    rand_num = random.choice([3,5,4,2])
    time.sleep(rand_num)
    print("Executin function in thread:", n)

#threadsList = []
for x in range(1, 6):
    t = threading.Thread(target = myFunc, args = (x,))  # agruments takes tuple. Since single element in the tuple, therefore ended with comma
    #threadsList.append(t)
    t.setDaemon(True)
    ''' when the above is uncommented, it makes all the threads t as the Daemon thread. Hence main thread is not waiting for them to end, to end itself.'''

    print("isDaemon:", t.isDaemon())  

    t.start()
    ##t.join()  '''uncommenting only this will make sure that all the child process will start execute one after another'''

#for tt in threadsList:
    #tt.join()