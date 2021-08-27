import multiprocessing

# new process is created. they have different/new process block assigned,
# hence different memory allocated.
# Hence, new copy of square_results list will be created for new process
# Thus program vars are not shared between two processes.
# We need IPC(Inter-Process communication) techniques to share data between two processes
# Since new process has its own thread, the result is stored in its own sq_res list
# If we print that process's list, then it will be ok, but it wont be same memory
# both lists will be different, although their result might be same(NOT happening in this prog, as on parent process, we are not calling calc_sq)

square_result = []

def calc_square(numbers):
    global square_result

    for n in numbers:
        print("square : " + str(n*n))
        square_result.append(n*n)
    print('Within a process: result ' + str(square_result))


if __name__ == '__main__':
    arr = [1,2,3,4,5]

    p1 = multiprocessing.Process(target = calc_square, args = (arr,))
    p1.start()
    p1.join()

    print("result : " + str(square_result))
    print("Done!!")