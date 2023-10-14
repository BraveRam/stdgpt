from OpsAi import Ai
import telebot

bot = telebot.TeleBot("6443205453:AAG_taKt4smj18dWj-1xq_994NAfZxNxzpk")

@bot.message_handler(commands=["start"], chat_types=["private", "supergroup"])
def go_out(message):
	bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(func = lambda message: True, chat_types=["supergroup"])
def answer(message):	
	if message.chat.username == "Furda_12th_Students":
		if message.text.startswith("/ask"):
			bot.send_chat_action(message.chat.id, "typing")
			req = Ai(query = message.text.split(maxsplit=1)[1])
			res = req.chat()
			bot.reply_to(message, res)
		elif message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id:
			bot.send_chat_action(message.chat.id, "typing")
			req = Ai(query = message.text)
			res = req.chat()
			bot.reply_to(message, res)
					
print("Successful")
bot.infinity_polling()
