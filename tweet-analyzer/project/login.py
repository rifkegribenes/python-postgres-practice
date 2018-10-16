import constants
import oauth2
import urllib.parse as urlparse
import json
from user import User
from database import Database

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

Database.initialize(database="learning",
                    user='sarahschneider',
                    password='Q-@VWfZPUbM3M5xCyRTu',
                    host="localhost")

user_email = input("Enter your email address: ")

user = User.load_from_db_by_email(user_email)

if user:
    pass
else:
    client = oauth2.Client(consumer)

    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print("An error occurred getting the request token from Twitter")


    request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    print("Go to the following site in your browser:")
    print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

    oauth_verifier = input("What is the PIN? ")

    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth2.Client(consumer, token)

    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    print(access_token)

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

# Create an 'authorized_token' Token object and use that to perform Twitter API calls on behalf of the user
authorized_token = oauth2.Token(user.oauth_token, user.oauth_token_secret)
authorized_client = oauth2.Client(consumer, authorized_token)

response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')
if response.status !=200:
    print('An error occurred while searching')

tweets = json.loads(content.decode('utf-8'))

for tweet in tweets['statuses']:
    print(tweet['text'])

