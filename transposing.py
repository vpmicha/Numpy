import numpy as np

scores = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88],
    [70, 65, 80]
])

#scores.shape == (4,3)
print(scores.shape)
#transposed scores.shape == (3,4)
'''scores = scores.T
print(scores)
print(scores.shape)'''
print(f'Student avg: {np.mean(scores, axis=1)}')
print(f'Subject avg: {np.mean(scores, axis=0)}')
print(f'Subject max: {np.max(scores, axis=0)}')
print(f'Student max: {np.max(scores, axis=1)}')


