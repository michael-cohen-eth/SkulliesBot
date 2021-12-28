# from rq import Queue
# from utils import cache
# from post import do_tweets

# q = Queue(connection=cache)

# def enqueue_job():
# 	q.enqueue(publish_tweets_job)

# def publish_tweets_job():
# 	event_strings = do_tweets()
# 	if len(event_strings) > 0:
# 		for event in event_strings:
# 			print(event)
# 	else:
# 		print("No new events. Sleeping...")