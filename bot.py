import os
import sys
import random

from api import line_bot_api, handler
from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)


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
    if event.message.text.find('101') > -1:
        message = TextSendMessage(text=random.choice(
            ['哇好高', '天阿好怕', '好討厭的感覺喔', '好想上觀景台喔', '觀景台門票好貴']))
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='好矮')
        line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
