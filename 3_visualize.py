import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

A = np.array([1, 0, 0])
B = np.array([0, 1, 0])
C = np.array([0, 0, 1])

AB = B - A
AC = C - A
normal = np.cross(AB, AC)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# --- 三角形 ---
ax.plot_trisurf(
    [A[0], B[0], C[0]],
    [A[1], B[1], C[1]],
    [A[2], B[2], C[2]],
    alpha=0.5,
    color='cyan'
)

# --- 点 A, B, C ---
ax.scatter(
    [A[0], B[0], C[0]],
    [A[1], B[1], C[1]],
    [A[2], B[2], C[2]], # type: ignore
    color='k',
    s=50
)

# 第3引数 zs は int | float と定義されている場合があるが、実際の matplotlib の実装ではzs に配列（list, ndarray）を渡すのが正しい使い方

ax.text(A[0], A[1], A[2], " A", color='k')
ax.text(B[0], B[1], B[2], " B", color='k')
ax.text(C[0], C[1], C[2], " C", color='k')

# --- 法線ベクトル（n） ---
ax.quiver(
    A[0], A[1], A[2],
    normal[0], normal[1], normal[2],
    color='r',
    length=1,
    normalize=True
)

# 法線ベクトルのラベル
ax.text(
    A[0] + normal[0] * 0.6,
    A[1] + normal[1] * 0.6,
    A[2] + normal[2] * 0.6,
    r"$\vec{n}$",
    color='r',
    fontsize=12
)

# --- 軸ラベル ---
ax.set_xlabel("X axis", color='red')
ax.set_ylabel("Y axis", color='green')
ax.set_zlabel("Z axis", color='blue')

# 表示範囲（見やすさ向上）
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_zlim(-0.5, 1.5)

ax.xaxis.label.set_color('red')
ax.tick_params(axis='x', colors='red')

ax.yaxis.label.set_color('green')
ax.tick_params(axis='y', colors='green')

ax.zaxis.label.set_color('blue')
ax.tick_params(axis='z', colors='blue') # type: ignore

plt.show()
