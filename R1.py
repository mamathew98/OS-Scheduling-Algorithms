import sys
import threading
import time


class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1
            
readLock = Semaphore(1)
writeLock = Semaphore(1)
readcnt = 0
class ReaderWriterProblem():
    def __init__(self,inputList):
        self.inputList = inputList


    def run(self):
        while (len(self.inputList)>0):
            for i in range(len(self.inputList)):
                self.inputList[i].run()
    
    
class Write():
        
    def __init__(self,number):
        
        self.number = number
            
    def run(self):
        try:
            writeLock.down()
            print(str(self.number) + "Writing!")
            #inputList.remove(self.number)
            time.sleep(0.1)
            writeLock.up()
        except:
            pass
            
            
class Read():

     def __init__(self,number):
          
          self.number = number
            

     def run(self):
         
        try:
            readLock.down()
            readcnt += 1
            if (readcnt == 1):
                writeLock.down
            readLock.up()
            print(str(self.number) + "Reading!")
            #inputList.remove(self.number)
            time.sleep(0.1)
            readLock.down()
            readcnt -= 1
            if (readcnt == 0):
                writeLock.up()
            readLock.up
        except:
            pass
           

r1 = Read(1)
r2 = Read(2)
r3 = Read(3)
w4 = Write(4)
r5 = Read(5)
T1 = ReaderWriterProblem([r1,r2,r3,w4,r5])
T1.run()
            
