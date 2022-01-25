import tweepy

from dataclasses import dataclass
from typing import Type
import argparse

TWEET_BAG_SIZE=100


# SIMPLE PERSISTENT SYSTEM TO FIX
import json

def save(datas) :
    with open('data.json', 'r') as file :
        savefile = json.load(file)
    savefile["datas"] = datas
    with open('data.json', 'w+') as file :
        json.dump(savefile, file)

def load():
    with open('data.json', 'r') as file :
        savefile = json.load(file)
        return savefile["datas"]



@dataclass
class tweet:
    id: str
    text: str = ""
    def __str__(self):
        return tweet.text

    def __repr__(self):
        return tweet.text


@dataclass
class user:
    id: str
    name: str = ""
    username:str = ""
    sizeofspeech: int=TWEET_BAG_SIZE   # This is an ugly design...    

    def __str__(self):
        return f"{self.username} ({self.name}): {self.id}"

    def __repr__(self):
        return f"{self.username} ({self.name}): {self.id}"

    def __eq__(self, other):
        return self.id == other.id

    @property
    def speech(self) -> str:
        if self.id == -1 :
            return ""
        print(max(10,self.sizeofspeech),)
        tweets = client.get_users_tweets(self.id,max_results=max(10,self.sizeofspeech), exclude="replies,retweets")
        tweetlist=[tweet(t.id, t.text) for t in tweets.data]
        return "\n".join([tweet.text for tweet in tweetlist])


class Twio:

    def __init__(self,token):
        self.client = tweepy.Client(bearer_token = token)
        

    def search_term(self,term, lang="fr"):
        text = term
        lang=lang
        query = f"({text}) lang:{lang}"
        data,includes,error,meta= self.client.search_recent_tweets(query=query, max_results=TWEET_BAG_SIZE,expansions="entities.mentions.username")
        
        
        #  Return both text and authors
        a= [t.text for t in data]
        b=[u.username for u in includes["users"]]
        return {"text":a, "authors":b}


    def speechof(self, user) :
        if user.id == -1 :
            return ""
        tweets = self.client.get_users_tweets(user.id,max_results=max(10,user.sizeofspeech), exclude="replies,retweets")
        tweetlist=[tweet(t.id, t.text) for t in tweets.data]
        return "\n".join([tweet.text for tweet in tweetlist])

    def getuser(self,username: str="EmmanuelMacron", sizeofspeech=TWEET_BAG_SIZE) ->Type[user]:
        try:
            res=self.client.get_user(username=username)
            return user(res.data.id, res.data.name, res.data.username,sizeofspeech)
        except Exception as e:
            return user(-1,"","")

