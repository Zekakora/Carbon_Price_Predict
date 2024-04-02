# 创建一个布尔矩阵
bool_matrix <- matrix(c(TRUE, FALSE, TRUE, TRUE, FALSE, FALSE), nrow = 2)

# 将布尔矩阵转换为 0-1 矩阵并保持原始形状
binary_matrix <- apply(bool_matrix, c(1, 2), as.integer)

print(binary_matrix)
