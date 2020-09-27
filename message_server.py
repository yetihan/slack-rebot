from flask import Flask
from flask import request
from slacker import Slacker

DEFAULT_CHANNEL = '#project-gakki'

with open('./web_hook_gakki',"r") as f:
    GAKKI_SLACK_WEBHOOK_URL = f.readline().strip()

slack = Slacker('', incoming_webhook_url=GAKKI_SLACK_WEBHOOK_URL)

def slack_nofity(text, channel=DEFAULT_CHANNEL, attachments=None):
    slack.incomingwebhook.post({
        'channel': channel,
        'text': text,
        'link_names': '1',
        'attachments': attachments
    })

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/msg')
def warn():
    text=request.args.get('text', 'None')
    channel= request.args.get('channel', '') or DEFAULT_CHANNEL 
    slack_nofity(text, channel)
    return "DONE"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
