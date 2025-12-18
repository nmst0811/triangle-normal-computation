# 3点の定義
A = [1, 0, 0]
B = [0, 1, 0]
C = [0, 0, 1]

# 辺ベクトル AB, AC
AB = [B[i] - A[i] for i in range(3)]
AC = [C[i] - A[i] for i in range(3)]

# 外積（法線ベクトル）
normal = [
    AB[1] * AC[2] - AB[2] * AC[1],
    AB[2] * AC[0] - AB[0] * AC[2],
    AB[0] * AC[1] - AB[1] * AC[0]
]

print("法線ベクトル:", normal)