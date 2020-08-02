# importing the module 
import json
import tweepy 

# personal details 
tweet_config = "jsons/tweet_config.json"
with open(tweet_config) as json_data_file:
    config = json.load(json_data_file)

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"]) 

# authentication of access token and secret 
auth.set_access_token(config["access_token"], config["access_token_secret"]) 
api = tweepy.API(auth) 

# update the status 
def tweet():
    try:
        api.update_status(status = config["tweet_body"])
        return ("OK")
    except Exception as e:
        return (str(e))

if __name__=="__main__":
    tweet()