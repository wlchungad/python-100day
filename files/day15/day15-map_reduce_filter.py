"""
    In HKDSE and JUPAS, there is a baseline of result, namely "3322"
    That is, a student should have at least level 3 in Chinese and English, level 2 in Maths and Liberal Studies
    Since Liberal Studies is cut by government, the following calculation will use the latest formula (i.e. no Liberal Studies)
"""

# Step 1: map for JUPAS Score
# in HKDSE, 5* means 6 and 5** means 7, so translation is required:
dict_hkdse_score = {
    'NULL': 0,
    'U':    0,
    '1':    1,
    '2':    2,
    '3':    3,
    '4':    4,
    '5':    5,
    '5*':   6,
    '5**':  7
}
# Assume a fixed weight schedule: Chinese, English, Math, and Major Elective 1 to 3
score_ratio = [1, 2, 2, 2, 1.5, 1]

example_records = [
    [3,3,4,4,3,3],
    [3,3,3,3,3,3],
    [3,3,2,2,2,2],
    [3,4,4,4,4,4],
    ['U',2,2,3,2,2],
    ['5**','5**','5**','5**','5**','5**'],
    [3,4,4,'5*','5*','NULL'],
    [3,4,4,4,4,4,4],
    [3,3,3,3,3,3,3,3],
    [2,2,2,2,5,5],
    [3,3,2,1,4,5]
]

# Step 2: filter whose fulfill the minimum requirements
def pass_minimum_requirement(score_list):
    score_list = score_list[0:5]
    # for 33xxxx
    if any(dict_hkdse_score[str(x)] < 3 for x in score_list[0:1]):
        return False
    # for xx22xx
    if any(dict_hkdse_score[str(x)] < 2 for x in score_list[2:]):
        return False
    return True
    return not(any(dict_hkdse_score[str(x)] < 3 for x in score_list[0:1]) or any(dict_hkdse_score[str(x)] < 2 for x in score_list[2:]))

phase_1_candidates = list(filter(pass_minimum_requirement, example_records))
print("Phase 1: those who pass the requirement of '3322':")
for i, _ in enumerate(phase_1_candidates): print((i+1), _)

# Step 3: calculate admission score (both raw and weighted)

def get_raw_admission_score(score_list):
    return sum([dict_hkdse_score[str(score_item)] for score_item in score_list[0:6]])

def get_weighted_admission_score(score_list):
    admission_sum = 0
    score_list = score_list[0:6]
    for i, single_score in enumerate(score_list):
        if type(single_score) == int:
            admission_sum += single_score * score_ratio[i]
        elif single_score == 'NULL':
            continue
        else:
            admission_sum += dict_hkdse_score[single_score] * score_ratio[i]
    return admission_sum

# JUPAS_score = [float(item) for item in JUPAS_score] 
#print(JUPAS_score)
raw_JUPAS_score = list(map(get_raw_admission_score, phase_1_candidates))
print("Raw sum:", raw_JUPAS_score)
weighted_JUPAS_score = list(map(get_weighted_admission_score, phase_1_candidates))
print("Weighted sum:", weighted_JUPAS_score)

# Assume the baseline admission score for a course is 24 (3C3X)
baseline = 24
def pass_baseline(n: float) -> bool: 
    return (n > baseline)

raw_interviewees = list(filter(pass_baseline, raw_JUPAS_score))
print("Those who pass the raw baseline score of %d: %s" % (baseline, raw_interviewees))
print(f"The average admission score is: {(sum(raw_interviewees)/len(raw_interviewees)):.1f}")

weighted_interviewees = list(filter(pass_baseline, weighted_JUPAS_score))
print("Those who pass the weighted baseline score of %d: %s" % (baseline, weighted_interviewees))
print(f"The average admission score is: {(sum(weighted_interviewees)/len(weighted_interviewees)):.1f}")