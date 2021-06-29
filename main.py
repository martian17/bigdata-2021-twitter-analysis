from requests_oauthlib import OAuth1Session
import json
import sys
import time



f = open("tokens.txt", "r")
[CONSUMER_KEY,
CONSUMER_SECRET,
ACCESS_TOKEN,
ACCESS_TOKEN_SECRET] = f.read().split("\n");
f.close();


def coxToCoords(box):
    if(box["type"] == "Polygon"):
        return box["coordinates"][0][0];
    if(box["type"] == "Point"):
        return box["coordinates"];
        

def getTweetCoordinates(tweet):
    if(tweet["coordinates"] != None):
        #print("a");
        #print(tweet["coordinates"]);
        return coxToCoords(tweet["coordinates"]);
    elif(tweet["place"] != None):
        #print("b");
        #print(tweet["place"]);
        place = tweet["place"];
        if(place["bounding_box"] != None):
            box = place["bounding_box"]
            return coxToCoords(box);
        raise Exception("error, no coordinates found");
    else:
        #print("c");
        #print(tweet["coordinates"]);
        #print(tweet["place"]);
        #print(tweet["geo"]);
        raise Exception("error, no coordinates found");

def getTweetText(tweet):
    if "full_text" in tweet:
        return tweet['full_text'].replace('\n', ' ')
    raise Exception("error, no full_text found");

def getTweetTime(tweet):
    if "created_at" in tweet:
        return tweet["created_at"]
    raise Exception("error, no created_at found");



twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/1.1/search/tweets.json"
params = {
    "q": sys.argv[2],
    "count": 10,
    "lang": "ja",
    "tweet_mode": "extended",
    # around Tokyo 1500 km
    "geocode": "35.6762,139.6503,1500km",
    #"result_type":"recent"
}
#params = {'q': "BigData", 'count': 10, 'lang': "jp", 'tweet_mode': "extended"}
res = twitter.get(url, params=params)
if res.status_code == 200:
    tweets = json.loads(res.text)
    #print(tweets);
    for tweet in tweets['statuses']:
        #print("");
        #print("");
        #print(tweet)
        #print(tweet['full_text'].replace('¥n', ' '))
        try:
            #coords = getTweetCoordinates(tweet)
            text = getTweetText(tweet);
            timestamp = getTweetTime(tweet);
        except:
            continue
        print("");
        print("");
        print(text);
        #print(coords);
        print(timestamp)# time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(timestamp)));
        #print(tweet['full_text'].replace('¥n', ' '))
else:
    print("ERROR: %d" % res.status_code)

# url = "https://stream.twitter.com/1.1/statuses/filter.json"
# req = twitter.post(
#     url,
#     stream=True,
#     data={
#         "track": sys.argv[2],
#         # Bounding box of Japan
#         #"locations":  "122.93361,20.42528,153.98639,45.55722",
#         #"language": "ja"
#     }
# )
# if req.status_code == 200:
#     count = 0;
#     for tweet in req.iter_lines():
#         try:
#             tweet = json.loads(tweet)
#             coords = getTweetCoordinates(tweet)
#             text = getTweetText(tweet);
#             timestamp = getTweetTime(tweet);
#         except:
#             continue
#         print("");
#         print("");
#         print(text);
#         print(coords);
#         print(time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(timestamp)));
# 
#         count = count + 1
#         if count >= int(sys.argv[1]):
#             break
# else:
#   print("ERROR: %d" % req.status_code)