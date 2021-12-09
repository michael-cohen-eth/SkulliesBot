from typing import Optional
import tweepy
import requests
from datetime import datetime
import os
from auth import get_twitter
from serializers import Event
from utils import get_env_key, get_cache, set_cache
import time


LAST_TIMESTAMP = "last_tweeted_event"

def get_asset_events(since: Optional[datetime] = None):
	# url = "https://api.opensea.io/api/v1/events?collection_slug=mutant-ape-yacht-club&event_type=successful&only_opensea=false&offset=0&limit=60"

	url = "https://api.opensea.io/api/v1/events?collection_slug=skulliesgmi&event_type=successful&only_opensea=false&offset=0&limit=60"
	if since:
		occured_after = f"&occurred_after={time.mktime(since.timetuple())}"
		url += occured_after
	headers = {
		"Accept": "application/json",
		"X-API-KEY": f"{get_env_key('OS_API_KEY')}"
	}

	response = requests.request("GET", url, headers=headers)
	events = response.json()
	# print(events)
	asset_events = events['asset_events']
	serialized = []
	for event in asset_events:
		serialized.append(Event.parse_obj(event))
		# print(f"raw: {event}")
	# events = any(event for event in serialized if event.asset.name == "Skullies GMI")
	# events = any(event for event in serialized)
	# for event in serialized:
	# 	print(event)
	return serialized

def get_event_string(event: Event):
	return f"{time.mktime(event.transaction.timestamp.timetuple())} || {event.asset.name} was summoned for {event.total_price / pow(10, event.payment_token.decimals)} {event.payment_token.symbol} by {event.winner_account.address} 🎲 💀 🎲 #skulliesgmi"


def get_last_tweeted_event() -> datetime:
	timestamp_str = get_cache(LAST_TIMESTAMP)
	return datetime.fromisoformat(timestamp_str) if timestamp_str else None

def set_last_tweeted_event(event: Event):
	set_cache(LAST_TIMESTAMP, str(event.transaction.timestamp))


def post_tweet(event: Event):
	twitter = get_twitter()
	try:
		# Create a tweet
		twitter.update_status(get_event_string(event))
		print("Tweet posted!")
		set_last_tweeted_event(event)
	except tweepy.TweepError:
		print('No update.')

