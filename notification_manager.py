#Telegram notification bot
import requests

bot_token = 'yourbottoken'
bot_chatID = 'yourchatid'

class NotificationManager:

    def __init__(self):
        pass

    def send_sms(self, message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                    + bot_chatID + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)
        # Prints if successfully sent.
        print(message)
        #print(response.json)
