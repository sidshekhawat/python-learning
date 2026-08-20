"""
multithreading = Used to perform multiple tasks concurrently (multitasking)
                 Good for I/O bound tasks like reading files or fetching data from APIs
                 threading.Thread(target=my_function)
"""

import threading
import time

def walk_dog(first_name):
    for i in range(1):
        time.sleep(8)
        print(f"Walking {first_name}")

def get_mail():
    for i in range(1):
        time.sleep(5)
        print("Getting mail...")

def play_with_dog(first_name):
    for i in range(1):
        time.sleep(10)
        print(f"Playing with {first_name}")

# Create threads for each task
walk_thread = threading.Thread(target=walk_dog, args=("Cookie",))
mail_thread = threading.Thread(target=get_mail)
play_thread = threading.Thread(target=play_with_dog, args=("Cookie",))

# Start the threads
walk_thread.start()
mail_thread.start()
play_thread.start()

# Wait for all threads to complete
walk_thread.join()
mail_thread.join()
play_thread.join() 

print("All tasks completed!")

