import sys
import threading
import time


class Philosopher(threading.Thread):

    def __init__(self, number, left, right, sem):
        threading.Thread.__init__(self)
        self.number = number
        self.left = left
        self.right = right
        self.sem = sem

    def run(self):
        for _ in range(1):
            self.sem.acquire()
            time.sleep(0.3)
            self.left.take(self.number)
            time.sleep(0.3)
            self.right.take(self.number)
            time.sleep(1)
            self.right.drop(self.number)
            self.left.drop(self.number)
            self.sem.release()

        sys.stdout.write("Process %s finished \n" % self.number)


class Fork(object):

    def __init__(self, number):
        self.number = number
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("Process %s took Fork %s\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("Process %s dropped Fork %s\n" % (user, self.number))
            self.lock.notifyAll()


def main():
    n = 5
    sem = threading.Semaphore(n - 1)
    f = [Fork(i) for i in range(n)]
    p = [Philosopher(i, f[i % n], f[(i + 1) % n], sem) for i in range(n)]

   # for i in range(n):
     #   p[i].start()

    s = [int(x) for x in input("PLz Enter Philosophers Id : ").split(" ")]
    for i in s :
        p[i].start()

    input()


if __name__ == "__main__":
    main()

