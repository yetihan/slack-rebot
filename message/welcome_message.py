import random
from .message import Message


class WelcomeMessageConfig:

    def __init__(self, header, text, image, at):
        self.header = header
        self.text = text
        self.image = image
        self.at = at


class WelcomeMessage(Message):

    def __init__(self):
        pass

    @staticmethod
    def create_message(msg_config):
        msg_template = WelcomeMessage.random__message()
        print(msg_template)
        return msg_template.format(header=msg_config.header,
                                   text=msg_config.text,
                                   image=msg_config.image,
                                   at=msg_config.at)

    @staticmethod
    def random__message():
        canditates = ['''[
            {{
                "type": "header",
                "text": {{
                    "type": "plain_text",
                    "text": "{header}",
                    "emoji": true
                }}
            }},
            {{
                "type": "section",
                "text": {{
                    "text": "{at} \\n {text}",
                    "type": "mrkdwn"
                }}
            }},
            {{
                "type": "image",
                "image_url": "{image}",
                "alt_text": "inspiration"
            }}
        ]''']
        return random.choice(canditates)


if __name__ == "__main__":
    header = "ようこそ！"
    text = "ようこそ ! 这是用来测试的！\\n こんにちは、新垣結衣です。お会いすることができてとても嬉しいです！ "
    image = "http://cms-bucket.nosdn.127.net/aabb4e241b714acb87a37c58bbd91c2f20170809204325.gif"
    at = "@zhou.han san"
    config = WelcomeMessageConfig(header, text, image, at)
    welcome_message = WelcomeMessage.create_message(config)
    from im.slack import Slack
    DEFAULT_CHANNEL = "ad-dynamic-ads-exp"
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
    slack = Slack(DEFAULT_CHANNEL, SLACK_WEBHOOK_URL)
    slack.slack.incomingwebhook.post({
        'channel': DEFAULT_CHANNEL,
        'blocks': welcome_message,
        'link_names': '1',  # no use right now
        'attachments': None
    })
