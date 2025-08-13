class InvalidScoreError(Exception):
   def __init__(self, score, message="Score must be between 0 and 100"):
      self.score = score
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return f"{self.message}. Provided age: {self.score}"

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return f"{self.message}. Provided age: {self.age}"

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

def set_score(score):
   if score < 0 or score > 100:
      raise InvalidScoreError(score)
   print(f"Test score is set to {score}")