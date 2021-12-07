import os
import requests
from post import get_asset_events

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/do', methods=['GET'])
def index_post():
    get_asset_events()
    return render_template('do.html')

@app.route('/callback', methods=['GET'])
def index_callback(oauth_token, oauth_token_secret, oauth_callback_confirmed):
    print(f"oauth_token: {oauth_token}")
    print(f"oauth_token_secret: {oauth_token_secret}")
    print(f"oauth_callback_confirmed: {oauth_callback_confirmed}")
    return render_template('callback.html')

if __name__ == '__main__': 
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
