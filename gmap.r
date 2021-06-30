# execute these when to install the requirements
# install.packages("RgoogleMaps")
# install.packages("ggmap")
# install.packages("stringr")
# and setup google api key here
# https://developers.google.com/maps/documentation/javascript/get-api-key
# it says JavaScript, but it works for r too.
# create project
# go to the following, make sure to change out the project_id with yours
# https://console.cloud.google.com/apis/library?project=your_project_id
# add Geocoding API and Maps Static API after searching
#
# note: you might need to turn on billing to avoid errors. Also give it time.
# Mine had to wait ~6 hrs to get it working.

# Thank you: https://stackoverflow.com/questions/47044068/get-the-path-of-current-script/47045368
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

library(ggmap)
library(stringr)

# create googlekey.txt and put your google api key that you created
fileName <- 'googlekey.txt'
api_key <- readChar(fileName, file.info(fileName)$size)
# cleaning the api key
api_key <- str_replace_all(api_key, "(^\\s+)|(\\s+$)","")

register_google(key=api_key)
map <- get_map(location = c(136.95665, 35.65892), zoom=5)


#chennai_places <- c("Kolathur",
#                    "Washermanpet",
#                    "Royapettah",
#                    "Adyar",
#                    "Guindy")

#places_loc <- geocode(chennai_places)

japan_places <- c("Tokyo",
                    "Kyoto",
                    "Osaka",
                    "Nagoya",
                    "Sendai")

places_loc <- geocode(japan_places)

#nomi <- read.csv("nomi.csv", header=F)
#jishuku <- read.csv("jishuku.csv", header=F)
nomi <- read.csv("nomi.csv")
jishuku <- read.csv("jishuku.csv")
#ggmap(map) + geom_point(data=nomi, aes(x=V2, y=V1), color='black') + 
#geom_point(data=jishuku, aes(x=V2, y=V1), color='red')
ggmap(map) + geom_point(data=nomi, color='black') + 
geom_point(data=jishuku, color='red')

write.csv(places_loc,"testtest.csv", row.names = FALSE)
testtest <- read.csv("testtest.csv")
