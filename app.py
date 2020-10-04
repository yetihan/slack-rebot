from config import Config
from logger import logger
from flask import Flask
from flask import request
from flask import Response
from flask import make_response

app = Flask(__name__)
bot = Config.create_bot()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/msg')
def msg():
    text = request.args.get('text', None)
    channel = request.args.get('channel', None)
    bot.send_msg_webhook(text, channel)
    return Response(status = 200)

@app.route("/slack_msg", methods=["GET", "POST"])
def slack_msg():
    slack_event = request.get_json()
    logger.debug(slack_event)

    # Slack URL Verification
    if "challenge" in slack_event:
        return make_response(
                slack_event["challenge"], 200, {"content_type":"application/json"}
            )

    # Slack Token Verification
    if bot.verification != slack_event.get("token"):
        message = f"Invalid Slack verification token: {slack_event['token']}"
        # adding "X-Slack-No-Retry" : 1 to turn off Slack's automatic retries during development.
        return make_response(message, 403, {"X-Slack-No-Retry": 1})

    # Process Incoming Events
    if "event" in slack_event:
        bot.get_msg(slack_event)
        return make_response("Event handler finished.", 200,)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
