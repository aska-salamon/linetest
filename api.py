from linebot import (LineBotApi, WebhookHandler)

# https://developers.line.me/console/
# Channel Access Token
line_bot_api = LineBotApi('PW01')
# Channel Secret
handler = WebhookHandler('USER01')
