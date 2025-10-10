import threading
import time

def print_numbers():
    time.sleep(3)
    print("1")
    time.sleep(2)
    print("2")

# Create a thread
t = threading.Thread(target=print_numbers)
t1 = threading.Thread(target=print_numbers)

# Start the thread
t.start()
t1.start()

# Wait for thread to finish
t.join()
print("hello")
t1.join()

print("Main thread finished.")
