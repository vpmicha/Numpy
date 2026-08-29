import numpy as np

scores = np.array([91,95,34,65,18,54,87,43,100,91])

print(f'MinScore: {np.argmin(scores)}')
print(f'MaxScore: {np.argmax(scores)}')
print(f'Mean: {np.mean(scores)}')
print(f'Median: {np.median(scores)}')
print(f'Mean: {np.mean(scores)}')
print(f'Standard deviation: {round(np.std(scores), 2)}')

passed = scores >= 50
passing_scores = np.where(scores>=50, scores, 'Fail')
print(passed)
print(passing_scores)

