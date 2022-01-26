# https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done {seconds} sec(S) of Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # We can use many methods with the executor object
    # If we want to execute function once at a time, then we use submit method
    # It schedules the function to be executed and returns a future object
    # future object encapsulates the execution of the function and allows to check in on it after its scheduled, to check if its running, or done, or if its done?
    
    
    # f1 = executor.submit(do_something, 1)
    # print(f1.result())    # it will wait here until function execution gets completed and return value gets received

    results = [executor.submit(do_something, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


    # However, using map function, it doesn't return future objects, but instead, it returns the result in the order the threads started
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s).')