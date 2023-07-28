import telebot,time
from telebot import types
TOKEN = '6431266693:AAE6KOjr78Mr-D_DKa43U6rTBqYSrmH_3SU'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
	a = types.InlineKeyboardButton('افضل بوتات التيليكرام 🤖🔥', url='t.me/botatkom')
	b = types.InlineKeyboardButton('اضافة الى مجموعه - add to group', url='https://t.me/d_xiim2bot?startgroup=true')
	c = types.InlineKeyboardMarkup()
	c.add(b)
	c.add(a)
	bot.send_message(message.chat.id,text=f'''<strong>
اهلا بك عزيزي 👤.
انا هو بوت تيليكرام 🤖،
وضيفتي هي منع السورسات والنشر التلقائي داخل المجموعات 🤖

اضفني الى المجموعه ثم ارفعني مشرف

المبرمج : @d_xiim
</strong>
	''', parse_mode='html', reply_markup=c)
def check_message(message):
	text = message.text.lower()
	if ".تكرار" in text and len(text) > 2 or ".مكرر" in text and len(text) > 2 or ".مؤقت" in text and len(text) > 2 or ".موقت" in text and len(text) > 2 or ".الاوامر" in text and len(text) > 2 or ".فحص" in text and len(text) > 2 or ".كتم" in text and len(text) > 2 or ".وقتي" in text and len(text) > 2 or ".حظر" in text and len(text) > 2 or ".سورس" in text and len(text) > 2 or ".بوت" in text and len(text) > 2 or ".سورسي" in text and len(text) > 2 or ".كت" in text and len(text) > 2 or ".اوامر" in text and len(text) > 2 or ".اوامري" in text and len(text) > 2 or ".منع" in text and len(text) > 2 or ".موقت" in text and len(text) > 2 or ".ترحيب" in text and len(text) > 2 or ".رحب" in text and len(text) > 2 or ".الترحيب" in text and len(text) > 2 or ".الترحيبات" in text and len(text) > 2 or ".تفعيل" in text and len(text) > 2 or ".اعاده تشغيل" in text and len(text) > 2 or ".اعاده" in text and len(text) > 2 or ".اعادة" in text and len(text) > 2:
		return True
	return False
@bot.message_handler(func=lambda message: True)
def handle_message(message):
	if check_message(message):
		last_name = message.from_user.full_name
		username = message.from_user.username
		id = message.from_user.id
		photos = bot.get_user_profile_photos(id).photos
		photo_file_id = None
		if photos:
			photo_file_id = photos[0][-1].file_id
		dev = types.InlineKeyboardButton('pro 👨‍💻', url='t.me/d_xiim')
		df = types.InlineKeyboardButton('افضل بوتات تيليكرام🤖🔥', url='t.me/botatkom')
		bb = types.InlineKeyboardMarkup(row_width=1);bb.add(dev)
		url = f'https://t.me/{username}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_file_id, caption=f'''
❖ - السورسات ممنوعه هنا 🎭

تم تقييد العضو {last_name} لانه خالف القوانين !

معلومات العضو المخالف !

[⌯] name ⌯ {last_name}
[⌯] user ⌯ @{username}
[⌯] id ⌯ {id}

مده التقييد نصف ساعه غير قابلة للتغير!
    ''', reply_markup=bb)
		chat_group = message.chat.id
		try:
			bot.restrict_chat_member(chat_group, id, can_send_messages=False)
		except:
			bot.send_message(chat_group,text='لا يمكنني تقييد مشرف !')
		time.sleep(1800)
		try:
			bot.restrict_chat_member(chat_group, id, can_send_messages=True)
			bot.send_message(chat_group,text=f'''
المستخدم {last_name} ، @{username}
تم فك التقيد عنك👤
			''')
		except:
			bot.send_message(chat_group,text=f'لا استطيع فك تقيد العضو @{username}')

bot.polling(True)