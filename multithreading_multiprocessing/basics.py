import time

def calc_square(numbers):
    print("Calculating sqaured numbers:")
    for n in numbers:
        time.sleep(0.5) # CPU is just doing nothing. Its lying idle
        print('square :', n*n)

def calc_cube(numbers):
    print("Calculating cubed numberes:")
    for n in numbers:
        time.sleep(0.5) # CPU is just doing nothing. Its lying idle
        print('Cube :', n*n*n)

arr = [1, 2, 3, 4, 5, 6, 7]

t = time.time()
calc_square(arr)
calc_cube(arr)
print('Done in :', time.time()-t)
print('Done!!!')