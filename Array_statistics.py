import numpy as np

scores = np.array([91,95,34,65,18,54,87,43,100,91,76,43,67,87,46])

print(f'MinScore: {np.min(scores)}')
print(f'MaxScore: {np.max(scores)}')
print(f'Mean: {round(np.mean(scores), 2)}')
print(f'Median: {np.median(scores)}')
print(f'Standard deviation: {round(np.std(scores), 2)}')

passed = scores >= 50
passing_scores = scores[scores >= 50]
print(passed)
print(passing_scores)

