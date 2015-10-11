library(ggplot2)
library(scales)
library(reshape)
library(plyr)

train0 = read.csv("D:/Workshop/homework/Data Analytics/Lab 4/train.csv")

train = train0[sample(nrow(train0), 100), ] #  Get a smaller training set randomly
train = train[,-1] #  Delete PassangerId
#train = str_replace(train[,4],"female",0) #  try to replace female and male as 0 and 1
#train = str_replace(train[,4],"male",1) #  Error in train[, 4] : incorrect number of dimensions
train$Name = with(train, reorder(Name, Survived)) #  Order by name and Survive
train.m = melt(train)
train.m = ddply(train.m, .(variable), transform, rescale = rescale(value))
p = ggplot(train.m, aes(variable, Name)) + geom_tile(aes(fill = rescale), colour = "white") + scale_fill_gradient(low = "white", high = "steelblue")
base_size = 9
p + theme_grey(base_size = base_size) + labs(x = "", y = "") + scale_x_discrete(expand = c(0, 0)) +
  scale_y_discrete(expand = c(0, 0)) + 
  theme(legend.position = "none", axis.ticks = element_blank(), axis.text.x = element_text(size = base_size *0.8, angle = 330, hjust = 0, colour = "grey50"))
train.s = ddply(train.m, .(variable), transform, rescale = scale(value))
last_plot() %+% train.s
