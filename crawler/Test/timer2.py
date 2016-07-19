import time
import threading
import random
def fun():
    for a in range(10):
        time.sleep(random.randint(1,5))
    print('end one tread')

threads = []

for _ in range(20):
    t = threading.Thread(target=fun)
    t.start()
    threads.append(t)
 
for t in threads:
    t.join()

print('all end')
