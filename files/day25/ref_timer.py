import time

length = 900

for t in range(length,0,-1):
    print(('{:02d}:{:02d}'.format(t // 60, t % 60)),end='\r')
    time.sleep(1)

