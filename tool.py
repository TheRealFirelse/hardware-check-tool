import psutil
import time

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    print(f"\rCPU: {cpu} | RAM: {ram}", end="", flush=True)
    time.sleep(2)
