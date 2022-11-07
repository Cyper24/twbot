import tweepy
from time import sleep

cl = tweepy.Client(
    consumer_key=" ",
    consumer_secret=" ",
    access_token=" ",
    access_token_secret=" "
)

f = open("list.txt", 'r')

for word in f:
   if word == "/n":
      continue   
   cl.create_tweet(text=word)
   print("Tweet Success")
   sleep(2)
