import time
class Countdown:
    def __init__(self, start:int = 10):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0: raise StopIteration
        current = self.start
        self.start -= 1
        time.sleep(1)
        return current
    
# bomb_countdown = Countdown(10)
# for count_time in bomb_countdown:
#     print(count_time)

class ExamCountdown(Countdown):
    def __init__(self, start:int = 10):
        super().__init__(start*60)

mathExam = ExamCountdown(15)
for count_time in mathExam:
    msg = ('{:02d}:{:02d}'.format(count_time // 60, count_time % 60))
    if count_time % 60 == 0 :
        msg += f" - {int(count_time/60)} minutes ({count_time}s) remaining"
    print(msg, end='\r')

print ("Time's up")