import telegram
from telegram.ext import Updater, MessageHandler
from telegram.ext import Filters
import lecfinder as lf

token = '5513740361:AAHKlEFGN8ySC7dLpkThZF4-XjnOjus-mSQ'
id = '5580001250'
bot = telegram.Bot(token=token)


# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "할일":  # 사용자가 보낸 메세지가 "안녕"이면?
        bot.send_message(chat_id=id, text='로딩중∙∙∙')
        report1 = lf.report1_result()
        report2 = lf.report2_result()
        video1 = lf.video1_result()
        video2 = lf.video2_result()
        quiz1 = lf.quiz1_result()
        quiz2 = lf.quiz2_result()
        bot.send_message(chat_id=id, text='{}\n{}'.format(report1, report2))
        bot.send_message(chat_id=id, text='{}\n{}'.format(video1, video2))
        bot.send_message(chat_id=id, text='{}\n{}'.format(quiz1, quiz2))

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
