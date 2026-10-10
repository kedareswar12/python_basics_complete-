import threading
import time 

def cpu_heavy():
  print("crunching some numbers ....")
  total = 0
  for i in range(10_000_000):
    total += 1
  print("done crunching numbers ....")
  
start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()

print(f"Total time taken {end-start:.2f} seconds")