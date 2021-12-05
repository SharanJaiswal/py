import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # print(f1.result())
    results = [executor.submit(do_something, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())






# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=(1.5, ))
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

finish = time.perf_counter()

print(f'Finished in round(finish-start, 2) seconds(s)')