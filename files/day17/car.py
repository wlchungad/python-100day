class Car():
    def __init__(self, brand="", model="", miles=0):
        self.brand = brand
        self.model = model
        self.miles = miles
    
    def start(self):
        print("Car started")
    
    def run(self):
        self.miles += 1
    
    def stop(self):
        print("Car stopped")
    
    def report(self):
        print(f"{self.brand} - {self.model} has run for {self.miles} miles")