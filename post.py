from typing import Optional
import tweepy
import requests
import datetime
import os
from serializers import Event, Asset

def get_env_key(key) -> Optional[str]:
	return os.environ[key] if key in os.environ else None

def get_asset_events():
	# url = "https://api.opensea.io/api/v1/events?collection_slug=mutant-ape-yacht-club&event_type=successful&only_opensea=false&offset=0&limit=60"
	url = "https://api.opensea.io/api/v1/events?collection_slug=skulliesgmi&event_type=successful&only_opensea=false&offset=0&limit=60"
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
	# events = any(event for event in serialized if event.asset.name == "Skullies GMI")
	# events = any(event for event in serialized)
	for event in serialized:
		print(event)
	# print(f"event info: {event}")
	return serialized

def get_event_string(event: Event):
	return f"{event.asset.name} was summoned for {event.total_price} {event.payment_token.symbol} by {event.to_account.address} 🎲 💀 🎲 #skulliesgmi"

# Authenticate to Twitter
# auth = tweepy.OAuthHandler("XXXX", "XXXX")
# auth.set_access_token("XXXX", "XXXX")

# # Create API object
# api = tweepy.API(auth)
# last_tweeted = api.user_timeline(count=1)[0].created_at

# for t in asset_events:
# 	print(t);
	# #for i in range(3):
	# 	ts = t['date'].strip()
	# 	print(ts)
	# 	post = "ago" in ts
	# 	if not post:
	# 		ts = datetime.datetime.strptime(ts, '%B %d %Y')
	# 		print(ts, last_tweeted)
	# 		post = last_tweeted < ts

	# 	if post:	
	# 		try:
	# 			# Create a tweet
	# 			api.update_status(f"{t['title']} by {t['artist']} is {t['tag'].upper()} on @Pitchfork. {t['title:link']} #{t['artist'].replace(' ','')} #pitchfork #bestnewmusic")
	# 		except tweepy.TweepError:
	# 			print('No update.')
