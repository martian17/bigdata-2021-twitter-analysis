from	requests_oauthlib import	OAuth1Session
import	json
CONSUMER_KEY  = "dhWo2QEM3P6gAP2S9vWHu8IQ0"
CONSUMER_SECRET = "4NMDpFnIHvOVgjMQurRxnizKdSPTv4daK1qk9cbi9sbMpNUaxv"
ACCESS_TOKEN  = "1176862254660079617-qEoVWY2c6hsYkAZRlDIKz2mqS9lzNZ"
ACCESS_TOKEN_SECRET = "i1sv5PLGvTAoNuTCYxJWER5t48jjwf4vVaIIiSRnM3FTy"
twitter	=	OAuth1Session(CONSUMER_KEY,	CONSUMER_SECRET,	ACCESS_TOKEN,	ACCESS_TOKEN_SECRET)
url =	"https://api.twitter.com/1.1/search/tweets.json"
params	=	{'q':	"#東京五輪は中止します",	'count':	10,	'lang':	"ja",	'tweet_mode':	"extended"}
res	=	twitter.get(url,	params=params)
if	res.status_code ==	200:
    tweets	=	json.loads(res.text)
    for	tweet	in	tweets['statuses']:
      print(tweet['full_text'].replace('¥n',	'	'))
else:
    print("ERROR:	%d"	%	res.status_code)