import os
from importlib import import_module

class Config(object):
    SYS_IM_TYPE = os.environ.get("SYS_IM_TYPE")

    DEFAULT_CHANNEL = os.environ.get("SLACK_DEFAULT_CHANNEL")
    SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
    SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
    SLACK_VERIFICATION = os.environ.get("SLACK_VERIFICATION")

    @staticmethod
    def create_bot():
        name = Config.SYS_IM_TYPE
        _class = import_module('im.' + name)
        if name == 'slack':
            return _class.SlackBot(Config.DEFAULT_CHANNEL, Config.SLACK_WEBHOOK_URL)



    
