library(ggplot2)
library(scales)
library(reshape)
library(plyr)

train = read.csv("D:/Workshop/homework/Data Analytics/Lab 4/train.csv")
head(train)

#boxplot(data = train, Age~Sex, main="Car Milage Data", xlab="Number of Cylinders", ylab="Miles Per Gallon") Distribution of age in Sex
#ggplot(train)+ geom_histogram(binwidth = 1,aes(x=Pclass, fill = ..count..)) + scale_fill_gradient("Count", low = "green", high = "red") + facet_grid(. ~ Survived) #  Survival in different class
#ggplot(train, aes(x = Age, y = Survived)) + geom_point() + facet_grid(Pclass ~ Sex) #  各年龄层中不同等级船舱男女的存活
#ggplot(train, aes(x = Age, y = Survived)) + geom_point() + facet_grid(Parch ~ Sex) #  各年龄层中不同直系血亲数量的男女的存活
#ggplot(train, aes(x = Age, y = Survived)) + geom_point() + facet_grid( SibSp~ Sex) #  各年龄层中不同直系血亲数量的男女的存活
#ggplot(train, aes(factor(Survived), Age)) + geom_violin(aes(fill = factor(Survived))) #  Distribution of age in survive 
