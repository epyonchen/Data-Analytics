setwd("D:/Workshop/homework/Data Analytics/Lab3/") #  Set directory
#install.packages("RSQLite") #perhaps needed
library("RSQLite")
sqlite = dbDriver("SQLite")
moviesDB = dbConnect(sqlite,"movies.db") #  Connect to database

query = dbSendQuery(moviesDB, "SELECT rate FROM MoviesInfo" ) #  Get each rate
rate = dbFetch(query, n = -1)
rate = rate[[1]]
query = dbSendQuery(moviesDB, "SELECT year FROM MoviesInfo" ) #  Get each year
year = dbFetch(query, n = -1)
year = year[[1]]
query = dbSendQuery(moviesDB, "SELECT vote FROM MoviesInfo" ) #  Get each vote
vote = dbFetch(query, n = -1)
vote = vote[[1]]
query = dbSendQuery(moviesDB, "SELECT PB FROM MoviesInfo" ) #  Get each Production Budget
PB = dbFetch(query, n = -1)
PB = PB[[1]]
query = dbSendQuery(moviesDB, "SELECT WG FROM MoviesInfo" ) #  Get each Worldwide Gross
WG = dbFetch(query, n = -1)
WG = WG[[1]]
query = dbSendQuery(moviesDB, "SELECT DG FROM MoviesInfo" ) #  Get each Democratic Gross
DG = dbFetch(query, n = -1)
DG = DG[[1]]
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo" ) #  Get all Information
moviesinfo = dbFetch(query, n = -1)
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 2010" ) #  Get movies after 2010
movies2010s = dbFetch(query, n = -1)
movies2010s[4] = 2010
print(movies2010s[1])
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 2000 AND year < 2010" ) #  Get movies between 2000 and 2010
movies2000s = dbFetch(query, n = -1)
movies2000s[4] = 2000
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1990 AND year < 2000" ) #  Get movies between 1990 and 2000
movies1990s = dbFetch(query, n = -1)
movies1990s[4] = 1990
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1980 AND year < 1990" ) #  Get movies between 1980 and 1990
movies1980s = dbFetch(query, n = -1)
movies1980s[4] = 1980
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1970 AND year < 1980" ) #  Get movies between 1970 and 1980
movies1970s = dbFetch(query, n = -1)
movies1970s[4] = 1970
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1960 AND year < 1970" ) #  Get movies between 1960 and 1970
movies1960s = dbFetch(query, n = -1)
movies1960s[4] = 1960
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1950 AND year < 1960" ) #  Get movies between 1950 and 1960
movies1950s = dbFetch(query, n = -1)
movies1950s[4] = 1950
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1940 AND year < 1950" ) #  Get movies between 1940 and 1950
movies1940s = dbFetch(query, n = -1)
movies1940s[4] = 1940
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1930 AND year < 1940" ) #  Get movies between 1930 and 1940
movies1930s = dbFetch(query, n = -1)
movies1930s[4] = 1930
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1920 AND year < 1930" ) #  Get movies between 1920 and 1930
movies1920s = dbFetch(query, n = -1)
movies1920s[4] = 1920
query = dbSendQuery(moviesDB, "SELECT * FROM MoviesInfo Where year >= 1910 AND year < 1920" ) #  Get movies between 1910 and 1920
movies1910s = dbFetch(query, n = -1)
movies1910s[4] = 1910
moviesdecades = rbind(movies1910s,movies1920s,movies1930s,movies1940s,movies1950s,movies1960s,movies1970s,movies1980s,movies1990s,movies2000s,movies2010s) # Rearrange movies in dacades
dbClearResult(query)

plot(PB, DG, main="Production Budget", xlab="Production Budget", ylab="Domestic Gross", pch=19) #  画散点图
abline(lm(DG~PB ), col="red") # regression line (y~x) #  根据散点图线性回归
cor(DG, PB) #  计算相关系数
#boxplot(PB~year,data=moviesdecades, main="Car Milage Data", xlab="Number of Cylinders", ylab="Miles Per Gallon")
library(ggplot2)
#gplot(moviesinfo,aes(x = PB))+ geom_histogram(aes(fill = ..count..)) #  x的总量直方图
#ggplot(moviesdecades, aes(factor(year), PB)) + geom_violin() #  PB在不同year上的分布
#ggplot(moviesinfo, aes(factor(round(rate, digits = 0)), vote)) + geom_violin() #  没懂什么意思

