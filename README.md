# Twitter Listener

A twitter bot to listen to certain users
The objective is to follow some bots on twitter that share their calls, and to replicate them on a trading exchange. 

## Setting up the .env file
You can set up the .env file with the following syntax:
```
TWITTER_CONSUMER_KEY=<your_consumer_key>
TWITTER_CONSUMER_SECRET=<your_consumer_secret>
TWITTER_ACCESS_TOKEN=<your_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>
BEARER_TOKEN=<your_bearer_token>
```
It will be used to authenticate on Twitter, using load_dotenv(). Of course, this file is git ignored for security reasons.