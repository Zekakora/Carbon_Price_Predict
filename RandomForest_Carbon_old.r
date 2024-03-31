library(randomForest)
library(lubridate)
library(ggplot2)
library(openxlsx)
library(dplyr)
library(isotree)
library(viridis)
library(gplots)
set.seed(123)
rm(list=ls())

data <- read.xlsx('data/bjtotal.xlsx')

# missing_matrix <- is.na(data)
# missing_matrix_numeric <- apply(missing_matrix,c(1,2),as.integer)
# # missing_matrix_numeric <- data.frame(missing_matrix_numeric)
data <- na.omit(data)
data$Time <- as.Date(data$Time)
data <- mutate_if(data, function(x) !is.Date(x), as.numeric)

# iso <- isolation.forest(data, ntrees = 500)
# pre <- predict(iso, data)
# temp <- matrix(missing_matrix_numeric, ncol = ncol(data))
# # colors <- c("black", "red")
# # 绘制热图
# dev.off()
# par(mai=c(1,1,1,1))  # 设置边距为 1 英寸
#
# # 绘制热图并拉伸
# heatmap.2(missing_matrix_numeric, Rowv = NA, Colv = NA, col = colors, scale = "none", main = "Missing Values Heatmap", dendrogram = "none", trace = "none", key = FALSE, keysize = NA)

# old_par <- par
# par(mfrow=c(4, 5)) # 创建4x4的图形布局
#
# for (col in names(data)) {
#   if (is.numeric(data[[col]])) { # 只绘制数值型列的箱线图
#     boxplot(data[[col]], main=col)
#   }
# }
#
# ggplot(data, aes(x = data$Time, y = data$Number)) +
#   geom_point(size = 1) +
#   labs(x = "Time", y = "Number") +
#   ggtitle("Scatter Plot of Number Over Time")+
#   theme_classic()

# 将数据转换为长格式
# data_long <- reshape2::melt(data, id.vars = "Time")
#
# # 创建散点图
# p<- scatter_plots <- ggplot(data_long, aes(x = Time, y = value)) +
#   geom_point() +
#   labs(x = " ", y = " ", title = "Data through Time") +
#   facet_wrap(~variable, scales = "free") +
#   theme_minimal()
# print(p)
# # 打印图形
# print(scatter_plots)