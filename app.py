from config import Config
from logger import logger
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
bot = Config.create_bot()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/msg')
def msg():
    text = request.args.get('text', None)
    channel = request.args.get('channel', None)
    bot.send_msg(text, channel)
    return Response(status = 200)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
