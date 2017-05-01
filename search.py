import time
import tweepy
import requests
import json
import urllib 
from flask import Flask, request, render_template, redirect, abort, flash, jsonify

app = Flask(__name__)

ftweet = ""

@app.route('/')
def search():
    #Google search api 
    google= 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDpn-CIoGwFwvyxSLSW6w0Bj-sc_J4MwEU&cx=001373588339273260243:hu2niwc7tyi&q=lectures'
    google_result = requests.get(google).content
    print google_result
    return google_result
    
    #Duck duck go search
    duck_duck_go = 'https://api.duckduckgo.com/?q=DuckDuckGo&format=json'
    response = requests.get(duck_duck_go).content
    print response
    return response
	
    #twitter search
    consumer_key = 'LwEgiTf74bGNg7JR72eDzyYgr'
    consumer_secret_key = 'bMfqEhnM4SHFoSzUR8B2WwMJmpOMrd4PzOPoIENeJyXDY9VKMR'
    access_token = '3317497801-pUPR3GathlC9jXcBU2xNnmfq2JraJoCLV9XZBXb'
    access_token_secret = 'KAm5xO3S5OhkZWTtZeSmsR4Yts9plhaITsEUZzGDQdYJU'
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key);
    auth.set_access_token(access_token,access_token_secret);
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print "lol nothing is working"
    api = tweepy.API(auth, timeout=1)
    tweet = api.search(q="dark knight",rpp = 1)
    count = 1
    ftweet = ""
    for check in tweet:
        if count == 1:
	    ftweet = ftweet+check.text
	    count = count + 1
	else: 
           break
     

if __name__ == '__main__':
	app.debug = True
	app.run()













































