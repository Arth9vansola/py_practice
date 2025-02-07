# 🔹 1. Multithreading (threading Module)
# Thread = A lightweight execution unit within a process.
# Multithreading = Running multiple threads within the same Python process.
# Best for: I/O-bound tasks (e.g., network requests, file I/O, database queries).
# Downside: Python’s Global Interpreter Lock (GIL) prevents true parallel execution of CPU-heavy tasks.

# # ✅ Example: Running Multiple Threads
# import threading
# import time

# def task(name):
#     print(f"Starting {name}...")
#     time.sleep(2)  # Simulate work
#     print(f"Finished {name}.")

# # Creating threads
# thread1 = threading.Thread(target=task, args=("Thread 1",))
# thread2 = threading.Thread(target=task, args=("Thread 2",))

# # Starting threads
# thread1.start()
# thread2.start()

# # Wait for threads to finish
# thread1.join()
# thread2.join()

# print("All threads completed.")

# 2. Multiprocessing (multiprocessing Module)
# Process = A separate instance of a program with its own memory space.
# Multiprocessing = Running multiple processes in parallel (bypasses the GIL).
# Best for: CPU-bound tasks (e.g., mathematical computations, data processing).
# Downside: Processes consume more memory than threads (each process has its own memory space).

# # ✅ Example: Running Multiple Processes
import multiprocessing
import time

def task(name):
    print(f"Starting {name}...")
    time.sleep(2)  # Simulate work
    print(f"Finished {name}.")

# Creating processes
process1 = multiprocessing.Process(target=task, args=("Process 1",))
process2 = multiprocessing.Process(target=task, args=("Process 2",))

# Starting processes
process1.start()
process2.start()

# Wait for processes to finish
process1.join()
process2.join()

print("All processes completed.")

