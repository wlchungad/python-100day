from car import *

x = Car("Tesla", "Model Y", 0)

x.start()

for i in range (100):
    x.run()

x.stop()

x.report()