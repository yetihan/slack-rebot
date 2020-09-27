Hi! I am a chat robot named Gakki.

You can execute the following code in any aws instance and you will receive a slack message in the given channel.

```
curl -i 'http://ip-10-1-18-31:5000/msg?text=test&channel=project-gakki'
curl -G -v http://ip-10-1-18-31:5000/msg --data-urlencode "text=I am Gakki."
curl -G -v http://ip-10-1-18-31:5000/msg --data-urlencode "text=I am Gakki."   --data-urlencode "channel=ad-ranking"
```

`text`(required)  is the message content, `channel`(optional) is the slack channel, default channel value is `project-gakki`.
