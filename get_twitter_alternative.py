import twitter
import jsonpickle

api = twitter.Api(consumer_key='',
	consumer_secret='',
	access_token_key='',
	access_token_secret='')

result = (api.GetSearch(raw_query="q=Manchester United&result_type=recent"))

writeFile(result, 'TweetRes.json')

def writeFile(tweets, fileName):
	f = open(fileName,'w')
	f.write('[\n')
	i = 0

	for tweet in tweets:
	    f.write('\t'+jsonpickle.encode(tweet._json,unpicklable=False))
	    if i < len(tweets)-1:
	    	f.write(',\n')
	    i += 1

	f.write('\n]')

