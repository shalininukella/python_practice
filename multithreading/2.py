import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create a thread
t = threading.Thread(target=print_numbers)
t1 = threading.Thread(target=print_numbers)

# Start the thread
t.start()
t1.start()

# Wait for thread to finish
t.join()
t1.join()

print("Main thread finished.")
