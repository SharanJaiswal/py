# https://lih-verma.medium.com/multi-processing-in-python-process-vs-pool-5caf0f67eb2b
# CPU multi-core programming, parallel programming/execution
# map(assigning the input task by division of inputs over cores) and reduce(aggragating the executed task to single output)

import multiprocessing
import time

def calc_square(num):
    sum = 0
    for x in range(10000):
        sum += x*x
    return sum

if __name__ == '__main__':
    
    t1 = time.time()

    p = multiprocessing.Pool()  # we can provide max processes limit for any given time by .Pool(processes=3)   This will limit processes to max 3 in numbers
    result = p.map(calc_square, range(10000))  # this alone can divide the work between the cores and give back the result in same order of an input
    p.close()
    p.join()

    print('Pool took : ', time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(calc_square(x))
    print('Serial processing time taken : ', time.time() - t2)