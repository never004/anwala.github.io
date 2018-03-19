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
#######################
#PROBLEM 3 STARTS HERE#
#######################
#slice genre data
item.data <- item[c(-1:-5)]
rownames <- rownames(item.data)
#invert and replace these rownames
t.item.data <- as.data.frame(t(item.data))
colnames(t.item.data) <- rownames
item.cors <- cor(t.item.data)
head(item.cors[c(1:6),c(1:6)])
#result in symmetric matrix
#make recommendations by item similarity
sub.me$movie.title <- item$movie.title[match(sub.me$item.id, item$movie.id)]
#now let's make a recommendation based off of similarity to Braveheart (22)
columnvector <- c(1:dim(item.cors))
thisdata <- as.data.frame(item.cors[22,])
rownames(head(thisdata[order(thisdata, decreasing=TRUE), , drop=FALSE], 10))
#function for getting top 5 movie recommendations based on item
top.5.items <- function(i.cors, i.id, u.id) {
  topuser <- data[data$user.id == u.id, ][c("item.id", "rating")]
  topdata <- as.data.frame(i.cors[i.id,])
  topdata <- topdata[-as.vector(topuser$item.id), , drop=FALSE]
  topdata <- topdata[-c(i.id), , drop=FALSE]
  rownames(head(topdata[order(topdata, decreasing=TRUE), , drop=FALSE], 5))
}
top.5.items(item.cors, 22, 45)
#results from the above line were
#"22" "188" "326" "515" "651"
#function for getting bottom 5 movie recommendations based on item
bottom.5.items <- function(i.cors, i.id, u.id) {
  bottomuser <- data[data$user.id == u.id, ][c("item.id", "rating")]
  bottomdata <- as.data.frame(i.cors[i.id,])
  bottomdata <- bottomdata[-as.vector(bottomuser$item.id), , drop=FALSE]
  bottomdata <- bottomdata[-c(i.id), , drop=FALSE]
  rownames(head(bottomdata[order(bottomdata, decreasing=FALSE), , drop=FALSE], 5))
}
bottom.5.items(item.cors, 22, 45)
#results from the above line were
#"560" "95" "141" "206" "302"
#now for users
top.5.user <- function() {
  cor.data.filtered <- correlateddata[correlateddata$incommon > 5, ]
  topdata <- head(cor.data.filtered[order(cor.data.filtered[,1], decreasing=TRUE), ], 5)
  rownames(topdata)
}
top.5.users <- top.5.user()
top.5.users
#results from the above line were
#"735" "68" "192" "235" "150"
bottom.5.user <- function() {
  cor.data.filtered <- correlateddata[correlateddata$incommon > 5, ]
  bottomdata <- head(cor.data.filtered[order(cor.data.filtered[,1], decreasing=FALSE), ], 5)
  rownames(bottomdata)
}
bottom.5.users <- bottom.5.user()
bottom.5.users
#results from the above line were
#"644" "553" "617" "567" "759"
#now let's combine users and items
top.5.user_items <- function(u.id, tar.id) {
  topuser <- data[data$user.id == u.id, ][c("item.id", "rating")]
  target <- data[data$user.id == tar.id, ][c("item.id", "rating")]
  items <- topuser[!(topuser$item.id %in% target$item.id),]
  items <- items[order(items[,2], decreasing=TRUE),]
  head(items$item.id, 5)
}
top.5.user_items(735,37)
#I use the value "735" here since it was the first value from top.5.users
#results from the above line were
#124 286 242 1 258
bottom.5.user_items <- function(u.id, tar.id) {
  bottomuser <- data[data$user.id == u.id, ][c("item.id", "rating")]
  target <- data[data$user.id == tar.id, ][c("item.id", "rating")]
  items <- bottomuser[!(bottomuser$item.id %in% target$item.id),]
  items <- items[order(items[,2], decreasing=FALSE),]
  head(items$item.id, 5)
}
bottom.5.user_items(735,37)
#results from the above line were
#289 325 741 100 283
get.ratings <- function(u.id, i.cors) {
  top.users <- top.5.user()
  #user suggestions and similar movies
  item.id <- unlist(lapply(top.users, top.5.user_items, tar.id=u.id))
  item.id <- append(item.id,
                    unlist(lapply(unique(item.id), top.5.items,
                                  u.id=37,
                                  i.cors=item.cors
                                  )
                           )
                    )
  #top movies
  topuser <- data[data$user.id == u.id,][c("item.id", "rating")]
  items <- topuser[order(topuser[,2], decreasing=TRUE),]
  my.top.10 <- head(items$item.id, 10)
  #similar top movies
  item.id <- append(item.id,
                    unlist(lapply(my.top.10, top.5.items,
                                  u.id=37,
                                  i.cors=item.cors
                                  )
                           )
                    )
  as.data.frame(table(item.id))
}
ratings <- get.ratings(37, item.cors)
#now for bottom
get.hatings <- function(u.id, i.cors) {
  bottom.users <- bottom.5.user()
  #user suggestions and similar movies
  item.id <- unlist(lapply(bottom.users, top.5.user_items, tar.id=u.id))
  item.id <- append(item.id,
                    unlist(lapply(unique(item.id), top.5.items,
                                  u.id=37,
                                  i.cors=item.cors
                                  )
                          )
                    )
  #bottom movies
  bottomuser <- data[data$user.id == u.id,][c("item.id", "rating")]
  items <- bottomuser[order(bottomuser[,2], decreasing=FALSE),]
  my.bottom.10 <- head(items$item.id, 10)
  #similar bottom movies
  item.id <- append(item.id,
                    unlist(lapply(my.bottom.10, top.5.items,
                                  u.id=37,
                                  i.cors=item.cors
                                  )
                          )
                    )
  as.data.frame(table(item.id))
}
hatings <- get.hatings(37, item.cors)
#how about we combine everything?
rec <- merge(x=ratings, y=hatings,
             by.x='item.id', by.y='item.id', all=T)
rec[is.na(rec)] <- 0
rec$total <- (rec$Freq.x - rec$Freq.y)
rec$movie.title <- item$movie.title[match(rec$item.id, item$movie.id)]