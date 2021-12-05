# import time

# # Since this program is executing it in procedural way, and since square func is called before cube
# # CPU is just doing nothing. Its lying idle between two square calculation. After that only it'll calls cube function
# def calc_square(numbers):
#     print("Calculating sqaured numbers:")
#     for n in numbers:
#         time.sleep(0.5)
#         print('square :', n*n)

# def calc_cube(numbers):
#     print("Calculating cubed numberes:")
#     for n in numbers:
#         # time.sleep(0.5) # CPU is just doing nothing. Its lying idle
#         print('Cube :', n*n*n)

# arr = [1, 2, 3, 4, 5, 6, 7]

# t = time.time()
# calc_square(arr)
# calc_cube(arr)
# print('Done in :', time.time()-t)
# print('Done!!!')




# Now the same program with threading

import threading
import time

def calc_square(numbers):
    print('Calculating squared numbers:')
    for num in numbers:
        time.sleep(0.4)
        print('square :', num * num)

def calc_cube(numbers):
    print('Calculating cubed numbers')
    for num in numbers:
        time.sleep(0.4)
        print('Cube :', num * num * num)

arr = [1, 2, 3, 4, 5, 6, 7]

start_time = time.time()

t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target=calc_cube, args=(arr, ))

t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()

end_time = time.time()

print('Total time taken is : ', end_time - start_time)