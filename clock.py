from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from auth import get_logged_in
from post import do_tweets

from utils import q

sched = BackgroundScheduler(timezone=utc)

@sched.scheduled_job('interval', hours=2)
def timed_job():
	if not get_logged_in():
		print("Not logged in, can't tweet...")
		return
		
	print('Enqueuing tweet job...')
	if get_is_enabled():
		enqueue_job()
	else:
		print("Scheduler disabled...")


def enqueue_job():
	q.enqueue(publish_tweets_job)

def publish_tweets_job():
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
		sched.shutdown()

sched.start(paused=True)