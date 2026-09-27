import time


maxRetries = 5
attempts = 0

waitTime = 1

while attempts < maxRetries:
    print(f"Attempt  {attempts + 1} wait time is  {waitTime}")

    time.sleep(waitTime) # sleeping
    waitTime *= 2

    attempts += 1
