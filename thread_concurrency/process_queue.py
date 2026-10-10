from multiprocessing import Process , Queue

q = Queue()

def prepare_chai(q):
  print("preparing the chai")
  q.put("chai is ready")
  
  
  
if __name__ == "__main__":
  p = Process(target=prepare_chai , args=(q,))
  p.start()
  p.join()
  
  print(q.get())