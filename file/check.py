from	requests_oauthlib import	OAuth1Session
import	json
import	sys
import	csv

CONSUMER_KEY  = "dhWo2QEM3P6gAP2S9vWHu8IQ0"
CONSUMER_SECRET = "4NMDpFnIHvOVgjMQurRxnizKdSPTv4daK1qk9cbi9sbMpNUaxv"
ACCESS_TOKEN  = "1176862254660079617-qEoVWY2c6hsYkAZRlDIKz2mqS9lzNZ"
ACCESS_TOKEN_SECRET = "i1sv5PLGvTAoNuTCYxJWER5t48jjwf4vVaIIiSRnM3FTy"

twitter	=	OAuth1Session(CONSUMER_KEY,	CONSUMER_SECRET,	ACCESS_TOKEN,	ACCESS_TOKEN_SECRET)
csvout =	csv.writer(sys.stdout)

url =	"https://stream.twitter.com/1.1/statuses/filter.json"
req =	twitter.post(url,	stream=True,	data={"locations":	sys.argv[2],	"language":	sys.argv[3]})
if	req.status_code ==	200:
  count	=	0;
  for	tweet	in	req.iter_lines():
    try:
        tweet	=	json.loads(tweet)
    except:
        continue
    if	tweet['geo']	==	None:
        continue
    if	tweet['geo']['type']	!=	"Point":
        continue
    if	"text"	in	tweet:
        csvout.writerow([tweet['geo']['coordinates'][0],	tweet['geo']['coordinates'][1],	tweet['text'].replace('¥n',	'	')])
        count	=	count	+	1
        if	count	>=	int(sys.argv[1]):
              break
else:
    print("ERROR:	%d"	%	req.status_code)