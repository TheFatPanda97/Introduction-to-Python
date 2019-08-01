import time

seconds = 0

while True:
    print(f"{seconds} seconds")
    seconds += 1
    time.sleep(1)
    print("\n" * 10)
