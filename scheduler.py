import time
def scheduler(f,n):
    time.sleep(n)
    f()

def hello_world():
    print("Hello World")

scheduler(hello_world,1)
