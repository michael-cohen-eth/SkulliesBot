from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

from queue import enqueue_job

sched = BackgroundScheduler(timezone=utc)

@sched.scheduled_job('interval', hours=2)
def timed_job():
	print('Enqueuing tweet job...')
	if get_is_enabled():
		enqueue_job()
	else:
		print("Scheduler disabled...")

def get_is_enabled() -> bool:
	return sched.running

def set_is_enabled(enabled: bool):
	if enabled:
		sched.resume()
	else:
		sched.pause()

sched.start()