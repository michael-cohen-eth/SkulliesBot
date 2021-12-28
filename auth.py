from typing import Optional, Tuple
import tweepy

from utils import get_cache, get_env_key, set_cache, del_cache

OAUTH_TOKEN = "oauth_token"
OAUTH_SECRET = "oauth_secret"
NAME = "TWITTER_NAME"

def set_auth(token: str, secret: str):
	set_cache(OAUTH_TOKEN, token)
	set_cache(OAUTH_SECRET, secret)

def get_auth() -> Tuple[Optional[str], Optional[str]]:
	return get_cache(OAUTH_TOKEN), get_cache(OAUTH_SECRET)


def get_twitter():
	token, secret = get_auth()
	if not token or not secret:
		raise "No auth set, can't tweet"

	# Authenticate to Twitter
	auth = tweepy.OAuthHandler(get_env_key("TWAUTH_APP_CONSUMER_KEY"), get_env_key("TWAUTH_APP_CONSUMER_SECRET"))
	auth.set_access_token(token, secret)

	# Create API object
	twitter = tweepy.API(auth)
	return twitter

def set_name(name: str):
	set_cache(NAME, name)

def get_name() -> Optional[str]:
	return get_cache(NAME)

def get_logged_in() -> bool:
	token, secret = get_auth()
	return token is not None and secret is not None

def logout_of_app():
	del_cache(OAUTH_TOKEN)
	del_cache(OAUTH_SECRET)
	del_cache(NAME)