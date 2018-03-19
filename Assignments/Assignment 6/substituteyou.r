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
rownames(u33.data) <- 1:nrow(u33.data)
u37.data <- data[data$user.id == 37, ][c("item.id", "rating")]
rownames(u37.data) <- 1:nrow(u37.data)
u66.data <- data[data$user.id == 66, ][c("item.id", "rating")]
rownames(u66.data) <- 1:nrow(u66.data)
#generate list of all ratings for each of the three
u33.data$item.id <- item$movie.title[match(u33.data$item.id, item$movie.id)]
u37.data$item.id <- item$movie.title[match(u37.data$item.id, item$movie.id)]
u66.data$item.id <- item$movie.title[match(u66.data$item.id, item$movie.id)]
#match item id to movie id
sub.me <- u37.data #chose user 37 as substitute me