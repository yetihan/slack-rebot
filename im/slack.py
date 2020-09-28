from logger import logger
from config import Config
from slacker import Slacker
from .interface import IM

class Slack(IM):

    def __init__(self, default_channel, webhook):
        self.default_channel = default_channel
        self.slack = Slacker('', incoming_webhook_url=webhook)
        logger.info(f'[Slack] default channel : {self.default_channel}')
        logger.info(f'[Slack] webhook : {webhook}')

    def send_msg(self, text, channel=None, attachments=None):
        self.slack.incomingwebhook.post({
            'channel': channel if channel else self.default_channel,
            'text': text,
            'link_names': '1',  # no use right now
            'attachments': attachments
        })

    def get_msg(self):
        pass
