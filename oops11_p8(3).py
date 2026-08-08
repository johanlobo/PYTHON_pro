class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds >=60:
            self.seconds = 0
            self.minutes += 1
        
        

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"


watch=Stopwatch()
for i in range(3601):
    print(watch)
    watch.tick()
   

    
#screw me!!!! wasted more than 30 mins finding a simple logic. 