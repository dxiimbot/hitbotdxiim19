import telebot,time,requests
from telebot import types

tnt = '6347831570:AAGuXjjkWyJ2Sm90oqGGZWF_FEaLqqOXmRc'
usersss =0
bot = telebot.TeleBot(tnt)

@bot.message_handler(commands=['start'])
def st(message):
	id = message.from_user.id
	fil = open('user.txt', "r").read()
	id_der = 5903160198
	full = message.from_user.full_name
	use = message.from_user.username
	if str(id) not in fil:
		global usersss
		usersss +=1
		bot.send_message(id_der,text=f'''
تم دخول عضو جديد للبوت 👾

رقم المستخدم : {usersss}
[~] اسمه : {full}
[~] يوزره : @{use}
[~] ايديه : {id}
		''')
		with open('user.txt', "a") as f:
			f.write(f'{id}\n')
	else:
		pass
	ch = types.InlineKeyboardButton('👾', url='t.me/d_xiim')
	mch = types.InlineKeyboardMarkup()
	mch.add(ch)
	bot.send_message(message.chat.id,text='''
• welcome dear 👤.
• I'm a telegram bot 🤖,
• And my guest is to fetch IP information 👨‍💻🔥

• send your ip 👾

developer : @d_xiim
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
• اهلا بك عزيزي 👤.
• انا هو بوت تيليقرام 🤖،
• وضيفتي هي جلب معلومات الـip 👨‍💻🔥

• ارسل الـip الخاص بك 👾

المطور : @d_xiim
	''',reply_markup=mch)
@bot.message_handler(func=lambda m:True)
def weather(message):
	msg = message.text
	try:
		url = requests.get(f'https://ipinfo.io/{msg}/geo').json()
		ip = url['ip']
		ci = url['city']
		reg = url['region']
		co = url['country']
		l = url['loc']
		org = url['org']
		tim = url['timezone']
		k = types.InlineKeyboardButton('افضل بوتات تيليكرام 🤖🔥', url='t.me/botatkom')
		kk = types.InlineKeyboardMarkup()
		kk.add(k)
		bot.send_message(message.chat.id, f'''
<strong>
done get info ip 🤖🔥

[⌯] where? ⌯ {l}
[⌯] country number ⌯ {co}
[⌯] city ⌯ {ci}
[⌯] region ⌯ {reg}
[⌯] org ⌯ {org}
[⌯] time zone ⌯ {tim}
</strong>
  ''',parse_mode='html',reply_markup=kk)
	except:
		bot.send_message(message.chat.id,'⚠️ ¦ ايبي غير صالح !')

bot.infinity_polling()