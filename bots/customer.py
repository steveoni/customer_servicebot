import tweepy
import logging
from config import create_api
import time
from pred import make_model
import re
from sendmail import send_mail

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def clean_tweet(tweet):
#     tweet = normalize('NFD', tweet).encode('ascii', 'ignore')
    tweet = str(tweet)
    tweet = re.sub('(RT\s(@\w+))', '', tweet)
    tweet = re.sub('@\\w+', '', tweet)
   
    tweet = re.sub('((http|https):(\S+))', '', tweet)
    tweet = re.sub('[!#?:*%$]', ' ', tweet)
    tweet = re.sub('[^\s\w+]', '', tweet)
    tweet = re.sub('[\n]', '', tweet)
    tweet = tweet.lower().strip()
    return tweet

def Mention(api,since_id,model):

    logger.info("Collecting info")

    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():

        new_since_id = max(tweet.id, new_since_id)

        text = clean_tweet(tweet.text) #clean the tweet
        pred = model.predict(text)[0] #make prediction

        print(str(pred))
        if str(pred) == "neg":

            name = tweet.user.screen_name
            status_id   =  tweet.id 
            link = f"https://twitter.com/{name}/status/{status_id}"
            resp = send_mail("steohenoni2@gmail.com",link)
            print(resp)

        
    return new_since_id

def main():
    api = create_api()
    since_id = 1206662450784944136
    model = make_model()
    while True:
        print(since_id)
        since_id = Mention(api,since_id,model)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()