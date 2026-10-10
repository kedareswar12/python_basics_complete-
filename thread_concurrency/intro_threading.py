import threading 
import time 

def take_orders():
  for i in range(1,4):
    print(f"taking order of {i}")
    time.sleep(2)
    
def brew_chai():
  for i in range(1,4):
    print(f"brewing the chai of {i}")
    time.sleep(3)
    
    
# process of creating the thread 
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)


order_thread.start()
brew_thread.start()



# once the thread is created it need to be stoped and then join 
"""
join here waits until the thread is terminated 

This blocks the calling thread until the thread whose join() method is called terminates -- either normally or through an unhandled exception or until the optional timeout occurs.

"""

# join the thread 
order_thread.join()
brew_thread.join()

print("All orders taken and brewed")