import os
import re
import json
import requests
from logger import logger
from config import Config
from slack import WebClient
from slack.webhook import WebhookClient, WebhookResponse
from .interface import IM

class SlackBot(IM):

    def __init__(self, default_channel, webhook):
        self.default_channel = default_channel
        self.wekbook_url = Config.SLACK_WEBHOOK_URL
        self.slack = WebClient(token=Config.SLACK_API_TOKEN)
        self.verification = Config.SLACK_VERIFICATION
        logger.info(f'[Slack] default channel : {self.default_channel}')
        logger.info(f'[Slack] webhook : {webhook}')

    def send_msg_webhook(self, text, channel=None, attachments=None):
        # self.slack.incomingwebhook.post({
        #     'channel': channel if channel else self.default_channel,
        #     'text': text,
        #     'link_names': '1',  # no use right now
        #     'attachments': attachments
        # })
        data = {
            'text': text,
            'channel': channel,
            'attachments': attachments,
            # 'username': 'HAL',
            # 'icon_emoji': ':robot_face:'
        }

        response = requests.post(self.wekbook_url, 
                        data=json.dumps(data), 
                        headers={'Content-Type': 'application/json'}
                    )

        logger.info('Response: ' + str(response.text))

    def send_msg(self, text, channel_id, attachments=None, thread_ts=None):
        post_message = self.slack.chat_postMessage(
                                            channel=channel_id,
                                            text=text,
                                            attachments=attachments,
                                            thread_ts=thread_ts
                                        )
        return post_message

    def get_msg(self, event):
        self._event_handler(event)

    def _event_handler(self, event):
        event_type = event["event"]["type"]
        team_id = event["team_id"]
        logger.debug(event_type)
        # [Events] : Team Join -> When the user first joins a team
        if event_type == "member_joined_channel":
            logger.info('Got [team_join] event!')
            user_id = event["event"]["user"]
            channel_id = event["event"]["channel"]
            msg = ("Welcome to Slack! Gakki so glad you're here. :two_hearts:"
                     "\nIf you have any question, please contact my big fans <@qiulu.zhang> :kissing_heart:")
            res = self.send_msg(f"<@{user_id}> {msg}", channel_id)

        # [Events] : App Mention -> If the user mention app
        elif event_type == "app_mention":
            logger.info('Got [app_mention] event!')
            user_id = event["event"]["user"]
            channel_id = event["event"]["channel"]
            thread_ts = event["event"]["ts"]
            org_text  = event["event"].get('text', '???')
            res = self.send_msg(f"<@{user_id}>{self._parse_msg(org_text)} :kissing_heart:", channel_id, thread_ts=thread_ts)

        # [Events] : Reaction Added -> If the user add an emoji reaction
        elif event_type == "reaction_added":
            logger.info('Got [reaction_added] event!')


        # [Events] : Pin Added -> If the user pin added a message
        elif event_type == "pin_added":
            logger.info('Got [pin_added] event!')

        # If the event_type does not have a handler
        else:
            message = "You have not added an event handler for the %s" % event_type
            logger.warn(message)

    def _open_conversation(self, user_id):
        new_dm = self.slack.conversations_open(users=[user_id])
        channel_id = new_dm["channel"]["id"]
        return channel_id

    def _parse_msg(self, text):
        # remove mention user
        return re.sub(r'<@.*>', ' ', text)

