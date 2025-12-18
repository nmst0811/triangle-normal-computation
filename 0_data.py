import csv
import random

N = 100000 # データ数

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ax", "Ay", "Az", "Bx", "By", "Bz", "Cx", "Cy", "Cz"])

    for _ in range(N):
        row = [random.random() for _ in range(9)]
        writer.writerow(row)