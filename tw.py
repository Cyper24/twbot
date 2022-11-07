import tweepy
from time import sleep

cl = tweepy.Client(
    consumer_key="FvwIRu0r9h2iEPMFfUKnIlDlM",
    consumer_secret="0wFHYx1ZNvrlfWuHDuJMLh4oFBy2JsJpAzLNcT1diU8uqw2v1b",
    access_token="1382180529563344897-FD6HlNZw64flgvK8W8sQTXeOr2ZarU",
    access_token_secret="dgIrQPWQ5vJAvIi2liPLfRBrSZTlJGBC6Cpz2Azw2s8uX"
)

f = open("list.txt", 'r')

for word in f:
   if word == "/n":
      continue   
   cl.create_tweet(text=word)
   print("Tweet Success")
   sleep(2)
