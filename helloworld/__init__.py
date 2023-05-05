import platform
import time

def main():
    first_time = True
    while True:
        if first_time:
            print("Hello, World!")
            print("Platform information:")
            print("-"*40)
            print(f"Operating system: {platform.system()}")
            print(f"Release: {platform.release()}")
            print(f"Version: {platform.version()}")
            print(f"Machine architecture: {platform.machine()}")
            first_time = False
        else:
            print('sleeping...')
            time.sleep(60)

main()
