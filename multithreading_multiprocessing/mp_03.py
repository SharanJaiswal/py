import multiprocessing

# We will use shared memory concept so that specific memories can be accessed by more than one processes
# There are two types of data structures here in this prog, that can be shared among processes; first is multiprocessing.Array & multiprocessing.Value

def calc_square(numbers, result, v):
    # since shared memory has not few special methods, hence we have to use index to access the shared array
    for idx, num in enumerate(numbers):
        print("square : " + str(num*num))
        result[idx] = num*num
    print('Within a process: result ' + str(result))  # This wont print the shared array element because it is not havig much functionality. BUT observe the memory address
    print(v)
    print(result[:], v.value)


if __name__ == '__main__':
    arr = [1,2,3,4,5]

    result = multiprocessing.Array('i', len(arr))   # i:integer, d:double, then size of array memory
    v = multiprocessing.Value('d', 0.1) # type then value holding by multiprocessing.Value variable

    p1 = multiprocessing.Process(target = calc_square, args = (arr, result, v))
    p1.start()
    p1.join()

    print("result : ", result)  # This wont print the shared array element because it is not havig much functionality. BUT observe the memory address
    print(v)
    print(result[:], v.value)
    print("Done!!")