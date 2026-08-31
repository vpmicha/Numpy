import numpy as np

scores = np.array([
    [81, 79, 90],
    [91, 62, 84],
    [51, 46, 57],
    [90, 90, 69]
])

bonus = np.array([[2],
                 [5],
                 [10],
                 [3]])

subject_bonus = np.array([[3,4,1]])

final_scores = scores + bonus + subject_bonus
print(np.shape(scores))