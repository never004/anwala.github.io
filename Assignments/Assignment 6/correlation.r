setwd('C:/users/nathaniel/appdata/local/programs/Assignment 6/')

user <- read.table('http://files.grouplens.org/datasets/movielens/ml-100k/u.user', sep="|", col.names = c("user id", "age", "gender", "occupation", "zip code"))
data <- read.table('http://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep="\t", col.names = c("user id", "item id", "rating", "timestamp"))
item <- read.table('http://files.grouplens.org/datasets/movielens/ml-100k/u.item', sep="|", fill=TRUE, col.names = c("movie id", "movie title", "release date", "video release date", "IMDb URL", "unknown", "Action", "Adventure", "Animation", "Childrens", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-fi", "Thriller", "War", "Western"), encoding = "ISO-8859-1", quote = "")
#read datasets into R dataframes
#NOTE: use quote = "" for reading u.item (because of single quotes)
df <- user[ which(user$age == 23
              & user$gender == 'M'
              & user$occupation == 'student'), ]
#generate subset, pick three
u33.data <- data[data$user.id == 33, ][c("item.id", "rating")]
u37.data <- data[data$user.id == 37, ][c("item.id", "rating")]
u66.data <- data[data$user.id == 66, ][c("item.id", "rating")]
#generate list of all ratings for each of the three
u33.data$item.id <- item$movie.title[match(u33.data$item.id, item$movie.id)]
u37.data$item.id <- item$movie.title[match(u37.data$item.id, item$movie.id)]
u66.data$item.id <- item$movie.title[match(u66.data$item.id, item$movie.id)]
#match item id to movie id
#######################
#PROBLEM 2 STARTS HERE#
#######################
user.list <- list() #gather list of data frames
for(n in 1:dim(user)) {
  user.list[[n]] <- data[data$user.id == n, ][c("item.id", "rating")]
}
#define a function for correlating the two data frames, cordf
cordf <- function(df.one, df.two) {
  df.one <- df.one[df.one$item.id %in% df.two$item.id,]
  df.two <- df.two[df.two$item.id %in% df.one$item.id,]
  df.one <- df.one[order(df.one[,1]),]
  df.two <- df.two[order(df.two[,1]),]
  cor(df.one$rating, df.two$rating)
}
sub.me <- data[data$user.id == 37, ][c("item.id", "rating")]
#chosen user 37 as sub.me from the substituteyou.r program
cordf(sub.me, user.list[[1]])
#now correlation with other users
cors <- list()
cors <- sapply(user.list, cordf, df.one=sub.me) #the first dataframe will be the substitute me
#sapply() will compare each user to sub.me
cors
#now to remove the NAs, find the largest value
cors[order(cors, decreasing=TRUE)]
#function to find number of movies used for correlation
movies.incommon <- function(df.one, df.two) {
  df.one <- df.one[ df.one$item.id %in% df.two$item.id, ]
  lengths(df.one)[1]
}
movies.incommon(sub.me, user.list[[1]])
incommon <- list()
incommon <- sapply(user.list, movies.incommon, df.one=sub.me)
head(incommon)
correlateddata <- data.frame(cors, incommon)
correlateddata <- correlateddata[-37,]
colnames(correlateddata) <- c("correlation", "incommon")
#we have some NAs, let's remove them
correlateddata <- na.omit(correlateddata)
correlateddata <- correlateddata[-37,]