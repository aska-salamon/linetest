from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
# )
from linebot.models import *

import random
food1=['唯斯','夏一跳','美好','劉姊姊','阿胖','小蘋果','永和豆漿','小餐車','美富美','美而美','薯霸','麥味登','阿婆','饅頭肉排蛋','阿根','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food2=['火雞肉飯','中華麵館','鐵皮屋','阿茂','鳳麟','超商','津香','金拱門','和味','大中華','昇一','四海','八方','牛肉麵','臭豆腐','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food3=['老兄','老家','八方','四海','六扇門','拿波里','大中華','滇味屋','義大利麵','東家','燒胖','唐揚雞塊','阿嬤壽司','素食','金拱門','肯德基','新豐餃子','德安','鴨香飯','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food4=['永豆','滷味','塊樂','蒜翻天','滿美','開源社','阿力','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
# google sheet start
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope=['https://spreadsheets.google.com/feeds']
# creds=ServiceAccountCredentials.from_json_keyfile_name('pythontest_clientsecret.json',scope)
# clients=gspread.authorize(creds)
# sheet=clients.open('pythontestupolad').sheet1

# google sheet end

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Dd7bX0CI0Z9Eq0AdVeR0j1yshQ+gtPdNepIH/16gvMuyL6uCFrmhAdNlmHuDOlpgl75xeWc+g9UvswshAOS3oj7WK9HliKZe3U1hKpIlP+iuS2e2SO1rm90BPukEWjA4irHtqjqNS6wpdTnfAbJk1AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f5e1ceddadbb1c5939fbbb09e3de1bd4')
#
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
    print(event.message.text)
    if event.message.text=='吃':
        buttons_template = TemplateSendMessage(
            alt_text='eat template',
            template=ButtonsTemplate(
                title='選三餐有障礙嗎?',
                text='你要吃哪餐',
                #thumbnail_image_url='',
                actions=[
                    MessageTemplateAction(
                        label='早餐',
                        text='早餐'
                    ),
                    MessageTemplateAction(
                        label='午餐',
                        text='午餐'
                    ),
                    MessageTemplateAction(
                        label='晚餐',
                        text='晚餐'
                    ),
                    MessageTemplateAction(
                        label='宵夜',
                        text='宵夜'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text=='早餐':
        get=random.sample(food1,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='午餐':
        get=random.sample(food2,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='晚餐':
        get=random.sample(food3,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='宵夜':
        get=random.sample(food4,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0

    # if event.message.text.find('吃')!=-1:
    #     message = TextSendMessage(text='甲~土~豆~~')
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         message)
    # else:
    #     message = TextSendMessage(text=event.message.text)
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         message)

import os
if __name__ == '__main__':
    app.run()
