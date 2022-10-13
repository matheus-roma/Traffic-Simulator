import threading, time

def target():
    i = 0
    while i < 11:
        print(f"First count to ten: {i}")
        time.sleep(2)
        i += 2
        
th = threading.Thread(target=target)
th.start()

for i in range(11):
        print(f"Second count to ten: {i}")
        time.sleep(1)