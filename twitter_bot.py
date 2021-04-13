# import
import tweepy as twp
import keys
import json

#Authenticate to twitter
auth = twp.OAuthHandler(keys.customer_key, keys.costumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = twp.API(auth)

try:
    api.verify_credentials()
    print("Authentication ok")
except:
    print("error during authentication")


#Info of users
user_name="elonmusk"
user = api.get_user(user_name)
print("User details:")
print(user.name)
print(user.description)
print(user.location)
print(user.followers_count)
print("\n\n")

#Get follower names
print("name of followers: ")
for follower in user.followers():
    print(follower.name)

#Get tweets of a user
tweets = api.user_timeline(screen_name= user_name, count = 10, include_rts= False)
for tw in tweets:
    print(tw.text)
    print(tw.created_at)


#Get tweets by hashtag
hashtag = "#ai"
tweets = twp.Cursor(api.search, q=hashtag, lang="en", include_rts=False).items(1)
for tw in tweets:
    # extract _json
    json_obj = tw._json

# pretty print
print(json.dumps(json_obj, indent=1))


