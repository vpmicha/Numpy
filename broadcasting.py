import numpy as np

bonus = np.array([[5,0,10]])

scores = np.array([[81,79,90],
                   [93,62,84],
                   [51,46,57],
                   [90,90,69]])

final_scores = scores + bonus
print(final_scores)
