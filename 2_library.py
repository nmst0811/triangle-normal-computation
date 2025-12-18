import numpy as np
import time

start = time.time()

data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

A = data[:, 0:3]
B = data[:, 3:6]
C = data[:, 6:9]

AB = B - A
AC = C - A

normals = np.cross(AB, AC)

end = time.time()
print("NumPy 実行時間:", end - start, "秒")