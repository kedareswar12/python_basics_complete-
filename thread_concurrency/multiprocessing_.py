from multiprocessing import Process
import time 


def brew_chai(name):
  print(f"Start of {name} brewing the chai")
  time.sleep(3)
  print(f"End of {name} brewing the chai")
  
  
if __name__  == "__main__":
  chai_makers = [
    Process(target=brew_chai , args=(f"chai maker #{i+1}",))
    for i in range (3)
  ]  
  # start the process 
  for p in chai_makers:
    p.start()
  
  # wait all the procees to complete 
  for p in chai_makers:
    p.join()
    
  print("all chais served")