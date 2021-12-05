import multiprocessing
import time

# If current running process are checked, then 3 processes will be shown
# one for square, one for cube, and one for main
def calc_square(numbers):
    for num in numbers:
        time.sleep(0.5)
        print('Square : ', num * num)

def calc_cube(numbers):
    for num in numbers:
        time.sleep(0.5)
        print('Cube : ', num * num * num)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]

    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr, ))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()