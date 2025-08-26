import random

def pretty_print(seq:zip):
    seq = list(seq)
    for i, elements in enumerate(seq):
        print (i, end=" ")
        for ele in elements:
            print(ele, end=" ")
        print()
        # for j, part in enumerate(element):
        #     print (f"{i}-{j} {part}")


SELECTION = ["Mathematics", "Science", "Language"]
# Create Tuples
students = ("James", "Mary",  "Michael","Patricia","John", "Jennifer", "Robert", "Linda", "David", "Elizabeth", "William", "Barbara")
# scores = (10, 20, 30) 
scores = tuple(random.randint(0,100) for _ in range(10))
studies = tuple(SELECTION[random.randint(0,2)] for _ in range(10))

# Zip students and scores (ignored "Jane"):
zipped_list = zip(students, studies, scores)
# Call pretty_print() with enum enabled:
pretty_print(zipped_list)