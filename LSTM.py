import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.ensemble import IsolationForest
from plotnine import *
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_excel('data/bjtotal.xlsx'))
data.dropna(inplace=True)



# 创建一个包含多个子图的画布
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))

# 将每个特征的箱线图绘制在相应的子图中
for i, col in enumerate(data.columns):
    ax = axes[i // 3, i % 3]  # 根据索引获取子图
    data[col].plot(kind='box', ax=ax)
    ax.set_title(col)  # 设置子图标题

plt.tight_layout()  # 调整子图布局，防止重叠
plt.show()
