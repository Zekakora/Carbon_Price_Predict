library(randomForest)
library(lubridate)
library(ggplot2)
library(gridExtra)
library(openxlsx)
library(dplyr)
library(isotree)
library(viridis)
library(gplots)
library(grid)
set.seed(123)
rm(list = ls())

missingvalue <- function() {
  # data <- read.xlsx('data/bjtotal.xlsx')
  # missing_matrix <- is.na(data)
  # missing_matrix_numeric <- apply(missing_matrix,c(1,2),as.integer)
  # missing_matrix_numeric <- data.frame(missing_matrix_numeric)
  # data <- na.omit(data)
  # data$Time <- as.Date(data$Time)
  # data <- mutate_if(data, function(x) !is.Date(x), as.numeric)
  #
  # iso <- isolation.forest(data, ntrees = 500)
  # pre <- predict(iso, data)
  # temp <- matrix(missing_matrix_numeric, ncol = ncol(data))
}

# 划分测试集与训练集
data <- read.xlsx('data/bjtotal.xlsx')
data <- na.omit(data)
data <- data[data$humi != 0,]
data <- select(data, -time)
data <- as.data.frame(lapply(data, as.numeric))

columns_to_process <- c("price", "pm2_5", "pm10", "so2", "complexindex", 'no2')

# 循环遍历每一列
for (col_name in columns_to_process) {
  # 创建箱线图并获取离群值
  OutVals <- boxplot(data[, col_name], plot = FALSE)$out

  # 删除包含离群值的行
  data <- data[!(data[, col_name] %in% OutVals), ]
}


index <- sort(sample(nrow(data), nrow(data) * .8))
train_data <- data[index,]
test_data <- data[-index,]

# 随机森林训练
price.train.forest <- randomForest(price ~ ., data = train_data, importance = TRUE)
price.train.forest
# # 使用训练集，查看预测精度
# price_predict <- predict(price.train.forest, train_data)
# result <- price_predict / train_data$price


imp_draw <- function() {
  # 绘图参数
  importance_price <- price.train.forest$importance
  importance_plot <- tibble(var = rownames(importance_price),
                            IncNodePurity = importance_price[, 2])
  importance_plot <- importance_plot %>% arrange(IncNodePurity)
  importance_plot$var <- factor(importance_plot$var, levels = importance_plot$var)

  importance_plotmse <- tibble(var = rownames(importance_price),
                               IncMSE = importance_price[, 1])
  importance_plotmse <- importance_plotmse %>% arrange(IncMSE)
  importance_plotmse$var <- factor(importance_plotmse$var, levels = importance_plotmse$var)

  # 绘制第一个子图
  p1 <- ggplot(importance_plot, aes(x = var, y = IncNodePurity)) +
    geom_segment(aes(x = var, xend = var, y = 0, yend = IncNodePurity), color = "skyblue") +
    geom_point(color = "blue", size = 4, alpha = 0.6) +
    theme_light() +
    coord_flip() +
    theme(
      panel.grid.major.y = element_blank(),
      panel.border = element_blank(),
      axis.ticks.y = element_blank()
    ) +
    labs(x = "Varible Name", subtitle = "IncNordPiority") # 设置子图的标题为空

  # 绘制第二个子图
  p2 <- ggplot(importance_plotmse, aes(x = var, y = IncMSE)) +
    geom_segment(aes(x = var, xend = var, y = 0, yend = IncMSE), color = "skyblue") +
    geom_point(color = "blue", size = 4, alpha = 0.6) +
    theme_light() +
    coord_flip() +
    theme(
      panel.grid.major.y = element_blank(),
      panel.border = element_blank(),
      axis.ticks.y = element_blank()
    ) +
    labs(x = "Varible Name", subtitle = "IncMSE") # 设置子图的标题为空

  # 创建组合图
  combined_plot <- grid.arrange(p2, p1, ncol = 2, top = textGrob("Variables Importance Based on RandomForest Model (without dataeval)", gp = gpar(fontsize = 14)))  # 设置组合图标题

  # 设置组合图标题字体加粗
  combined_plot$top <- gList(combined_plot$top, top = textGrob("Variables Importance Based on RandomForest Model (without dataeval)", gp = gpar(fontsize = 20, fontface = "bold")))
  # 显示组合图
  print(combined_plot) }