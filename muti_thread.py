import threading
import time

def my_function(a, b):
    # Code to be executed in the thread
    while True:
        b += 1
        time.sleep(1)
        print(a, b)

# Create a new thread
my_thread1 = threading.Thread(target=my_function, args=('a', 100))
my_thread2 = threading.Thread(target=my_function, args=('b', 100))

# Start the thread
my_thread1.start()
my_thread2.start()

my_thread1.join()

# Wait for the thread to finish

my_thread2.join()