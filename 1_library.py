import numpy as np

A = np.array([1, 0, 0])
B = np.array([0, 1, 0])
C = np.array([0, 0, 1])

AB = B - A
AC = C - A

normal = np.cross(AB, AC)

print("法線ベクトル:", normal)
