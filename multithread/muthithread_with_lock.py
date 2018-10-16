import threading

x = 0

def increment():
    global x
    x += 1

def thread_task(lock):
    lock.acquire()
    print "thread acquired lock = {} and x value is = {}".format(threading.current_thread().name, x)
    increment()
    lock.release()

def main_task():
    global x
    #x = 0
    lock = threading.Lock()

    for _ in range(5):
        t1 = threading.Thread(target=thread_task, args=(lock,), name='t1')
        t2 = threading.Thread(target=thread_task, args=(lock,), name='t2')

        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == "__main__":
    main_task()
    print "Done"
