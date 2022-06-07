import threading

def createThread(f: callable, *a: any):
    t = threading.Thread(target=f, args=a)
    t.daemon = True
    t.start()
    return t