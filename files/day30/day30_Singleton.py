import logging

class SingletonLogger(logging.Logger): 
    _instance = None 
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
        return cls._instance 
         
    def __init__(self, name, level=logging.NOTSET): 
        super().__init__(name, level) 


logger1 = SingletonLogger("Test", logging.INFO)

print (f"logger1: {id(logger1)}")
logger1.info(f"{id(logger1)}: This is a test INFO message.")
logger1.warning(f"{id(logger1)}: This is a test WARN message.")
logger1.error(f"{id(logger1)}: This is a test ERROR message.")
# logger1.exception(f"{id(logger1)}: This is a test EXCEPTION message.")



logger2 = SingletonLogger("Test", logging.INFO)
print (f"logger2: {id(logger2)}")

exit(0)