import datetime as dt 

import winsound

class Alarm:
    
    def __init__(self,h=0,m=0,s=0):
        self.h = h 
        self.m = m
        self.s = s
        self.time = f'{self.h}:{self.m}:{self.s}'
    
    def sound(self):
        frequency= 100
        duration = 1000
        for i in range(6):
            winsound.Beep(frequency, duration)
            frequency+=100
            duration+=40
    
    def check(self):
        while True:
            t=0
            recent_time = dt.datetime.now().strftime('%#H:%#M:%#S')
            if self.time == recent_time: 
                return self.sound() 
                break
            t=t-1

a=Alarm(19,47,11)        
a.check()


