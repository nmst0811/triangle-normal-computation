import csv
import time

start = time.time()

normals = []

with open("data.csv", "r") as f:
  reader = csv.DictReader(f)
  for row in reader:
    A = [float(row["Ax"]), float(row["Ay"]), float(row["Az"])]
    B = [float(row["Bx"]), float(row["By"]), float(row["Bz"])]
    C = [float(row["Cx"]), float(row["Cy"]), float(row["Cz"])]

    AB = [B[i] - A[i] for i in range(3)]
    AC = [C[i] - A[i] for i in range(3)]

    normal = [
        AB[1] * AC[2] - AB[2] * AC[1],
        AB[2] * AC[0] - AB[0] * AC[2],
        AB[0] * AC[1] - AB[1] * AC[0]
    ]

    normals.append(normal)

end = time.time()
print("基本文法 実行時間:", end - start, "秒")
