from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

from post import do_tweets
from utils import get_env_key
from queue import q

sched = BackgroundScheduler(timezone=utc)

@sched.scheduled_job('interval', hours=2)
def timed_job():
	print('Enqueuing tweet job...')
	q.enqueue(publish_tweets_job)

def publish_tweets_job():
	if not get_is_enabled():
		print("Scheduler disabled...")
		return
	event_strings = do_tweets()
	if len(event_strings) > 0:
		for event in event_strings:
			print(event)
	else:
		print("No new events. Sleeping...")

def get_is_enabled() -> bool:
	return sched.running

def set_is_enabled(enabled: bool):
	if enabled:
		sched.resume()
	else:
		sched.pause()

sched.start()