import threading
import time


# Define a function that takes arguments
def print_numbers(start, end):
    print(threading.current_thread().name + " Started!")
    for i in range(start, end):
        # print(f"Thread {threading.current_thread().name}: {i}")
        continue
        # time.sleep(1)
    print(threading.current_thread().name + " Ended!")


# Create a thread with arguments
thread1 = threading.Thread(target=print_numbers, args=(1, 100), name="Thread 1")
thread2 = threading.Thread(target=print_numbers, args=(1, 100), name="Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished execution.")
