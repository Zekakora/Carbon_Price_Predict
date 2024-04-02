import pandas as pd
import matplotlib.pyplot as plt

# 创建一个示例DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# 获取列数
num_cols = len(df.columns)

# 创建子图
fig, axes = plt.subplots(num_cols, 1, figsize=(8, num_cols*4))

# 循环绘制每一列的散点图
for i, col in enumerate(df.columns):
    ax = axes[i] if num_cols > 1 else axes
    ax.scatter(range(len(df)), df[col])
    ax.set_title(col)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
