# SkullieBot, an OpenSea sales Twitter bot for ProbCause's Skullies GMI project

This repo contains the code running the [SkullyBot twitter account](https://twitter.com/SKULLY_BOT) Twitter bot, which tweets whenever new sales are generated for ProbCause's Skullies GMI NFT collection. Inspired **heavily** by [BotPitchfork](https://twitter.com/BotPitchfork)

The bot is built using the [OpenSea API](https://docs.opensea.io/reference) and [Tweepy](http://tweepy.org).
Everything is hosted on Heroku, with a Flask app.

## Description

A detailed description of the project can be found [on Medium](https://medium.com/analytics-vidhya/building-a-twitter-bot-with-any-data-using-dashblock-and-tweepy-fd2b9f7ff5fc).


### Development Setup
- `pipenv install`

- `pipenv shell`

- `python app.py`

## Hosting 

The template used to host the Flask app on Heroku comes from:
https://github.com/yefim/flask-heroku-sample.

There you will also find instructions on how to deploy to Heroku.

## Handoff

Before handing off, will need to provide ProbCause with the following:
- Access to Twitter API acct
- Access to Heroku acct
- Access to this repo codebase

Will need to switch out the following info:
- CC info on heroku

