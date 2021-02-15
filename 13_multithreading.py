from concurrent.futures import ThreadPoolExecutor
import time

devices = ['PHRCRG1', 'PHRCSL05F03', 'PHRCSL38F21', 'PHRCSH1', 'PHRCSL07F05']

def network_task(device):
    print(f"STARTING TASK :: {device}")
    time.sleep(5)
    print(f"TASK COMPLETE :: {device}")

start_time = time.time()
for device in devices:
    network_task(device)
end_time = time.time() - start_time
print(f"Sequential finished in {end_time} seconds\n\n")

start_time = time.time()
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(network_task, devices)
end_time = time.time() - start_time
print(f"Multithreading finished in {end_time} seconds")

