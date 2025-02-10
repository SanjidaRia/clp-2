import numpy as np
RandomValues = np.random.rand(130) 
normalized_values = (RandomValues - np.min(RandomValues)) / (np.max(RandomValues) - np.min(RandomValues))
print(normalized_values)