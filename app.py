from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('nx/QJURYoJp5itwu/0T4gf+ZIwuRIrT4UczQpu7j0KnZTQ8Ufjky5Th2fUGiv+4Al75xeWc+g9UvswshAOS3oj7WK9HliKZe3U1hKpIlP+hjtu+Qf8WCoH0UFD2HzjVfeKMMlRefiRM37MEQVXEN+wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('adf2f8c258655ed50846780126dd4a71')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    app.run()
