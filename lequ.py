import numpy as np
import numpy.linalg as LA

# 連立方程式Ax=bを解く
a = np.array(
    [
        [1, 1, 1, 1], [1, 1, 1, -1], [1, 1, -1, 1], [1, -1, 1, 1]
    ]
)
b = np.array(
    [0, 4, -4, 2]
)
ans = np.dot(np.dot(LA.inv(np.dot(a.T, a)), a.T), b)
print(ans)
