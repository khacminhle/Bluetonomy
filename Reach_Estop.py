import time
import threading


class Reach_Estop_Class:
    def __init__(self) -> None:
        self.event = threading.Event()
        self.flag = False
        
    

    def run(self): 
        while True:
            self.checktemp()
            self.checktorque()

    def pulse(self):
        while True:
            self.event.set()
            self.event.clear()
            time.sleep(10)
            
            
        

    def checktorque(self): #Check for the reading of torque during, will need to time it so that when checking for tolerance it isnt using the same path
        self.mutex.acquire()

        self.mutex.release()

    def checktemp(self):
        pass




if __name__ == "__main__":
    kin = Reach_Estop_Class()
    kin.run()