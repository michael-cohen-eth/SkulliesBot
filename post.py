from typing import List, Optional
import tweepy
import requests
from auth import get_twitter
from serializers import Event
from utils import get_cache_int, get_env_key, set_cache


LAST_TIMESTAMP = "last_tweeted_event"

def get_asset_events(since: Optional[int] = None):
	url = "https://api.opensea.io/api/v1/events?collection_slug=skulliesgmi&event_type=successful&only_opensea=false&offset=0&limit=60"
	if since:
		occured_after = f"&occurred_after={since}"
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
	serialized.sort(key=lambda x: x.transaction.time_occurred)

	return serialized

def get_event_string(event: Event):
	return f"{event.asset.name} was summoned for {event.total_price / pow(10, event.payment_token.decimals)} {event.payment_token.symbol} by {event.winner_account.address} 🎲 💀 🎲 #skulliesgmi {event.asset.permalink}"


def get_last_tweeted_event() -> int:
	return get_cache_int(LAST_TIMESTAMP)

def set_last_tweeted_event(event: Event):
	current = get_last_tweeted_event()
	if current and current > event.transaction.time_occurred:
		print("Currently stored timestamp is ahead of this event. Not updating.")
		return
	print(f"Setting {LAST_TIMESTAMP} cache to {str(event.transaction.time_occurred)}")
	set_cache(LAST_TIMESTAMP, str(event.transaction.time_occurred))


def post_tweet(event: Event):
	twitter = get_twitter()
	try:
		# Create a tweet
		if get_env_key("TESTING", "true") == "true":
			print("Not posting tweet. Testing mode.")
		else:
			print(f"Posting tweet: {get_event_string(event)}")
			twitter.update_status(get_event_string(event))
		
		print("Tweet posted!")
		set_last_tweeted_event(event)
	except tweepy.TweepyException:
		print('No update.')


def do_tweets() -> List[str]:
	since = get_last_tweeted_event()
	events = get_asset_events(since=since)
	event_strings = [get_event_string(event) for event in events]
	for event in events:
		post_tweet(event)
	return event_strings