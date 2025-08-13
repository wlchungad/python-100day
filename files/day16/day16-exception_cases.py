from exceptions import *
import random
examples = [ [0, 0], [100, 100], [200,200], [18, 50], [30, 75], [40, '60'], [99, 99] ]

for _ in range(100):
    examples.append([random.randint(0,200), random.randint(0, 200)])
print(len(examples))
for i,x in enumerate(examples):
    try:
        print(f"Record {i}: {x}")
        set_age(x[0])
        set_score(x[1])
    except InvalidAgeError as excp_age:
        print(f"Invalid age {excp_age.age}: {excp_age.message}")
        examples.remove(x)
        continue
    except InvalidScoreError as excp_score:
        print(f"Invalid score {excp_score.score}: {excp_score.message}") 
        examples.remove(x)
        continue
    except Exception as e:
        print(f"Other Error in record {x}: {e}")
        examples.remove(x)
        continue
    
# import matplotlib.pyplot as plt
# plt.scatter([x[0] for x in examples], [x[1] for x in examples])
# plt.show()
avg_age = sum(i[0] for i in examples) / len(examples)
avg_score = sum(i[1] for i in examples) / len(examples)
print("After cleansing, the average age & score of %d records: %d, %d" % (len(examples), avg_age, avg_score))
