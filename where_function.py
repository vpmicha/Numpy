import numpy as np

scores = np.array([
    [80, 45, 91],
    [62, 88, 39],
    [95, 73, 84]
])

positions = np.where(scores>=90)
positions_rows = positions[0]
positions_columns = positions[1]
print(positions_rows)
print(positions_columns)
boolean_scores = scores >= 50
labels = np.where(boolean_scores, 'Pass', 'Fail')
print(labels)
scores = np.where(scores<50, 50, scores)
print(scores)

