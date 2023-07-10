import os

import datetime

import requests

import gdolib

import random

import telebot

import threading

from AegosPy import *

from telebot import *

from time import sleep

import os

import random

import requests

import user_agent

import json

import uuid

import re

import mechanize

from user_agent import generate_user_agent

#now = datetime.datetime.today()

#mm = str(now.month)

#dd = str(now.day)

#yyyy = str(now.year)

#hour = str(now.hour)

#mi = str(now.minute)

#ss = str(now.second)

#hours = (now.hour)

token = '6139875501:AAEqAZkvV-Bg8nydl9mxABAmYF_ePRrZ5go'

#now = datetime.datetime.today()

#now = datetime.datetime.today()

bot = telebot.TeleBot(token)

list = '1234567890poiuytrewqasfdghjklmnbvcxz'

list_num = '456789'

dergham = 5903160198, 5842261151 

gmail = 0

yahoo = 0

hotmail = 0

aol = 0

mailru = 0

bad1 = 0

bad2 = 0

bad3 = 0

bad4 = 0

bad5 = 0

bad11 = 0

bad22 = 0

bad33 = 0

bad44 = 0

bad55 = 0

bad111 = 0

bad222 = 0

bad333 = 0

bad444 = 0

bad555 = 0

bad1111 = 0

bad2222 = 0

bad3333 = 0

bad4444 = 0

bad5555 = 0

@bot.message_handler(commands=['id', 'Id', 'iD', 'ID'])

def owbe(mo):
	
	ig = mo.from_user.id
	
	a = '1234567890poiuytrewQWERTYUIOPLKJHGFDSAZXCVBNMqasdfghjklmnbvcxz'
	
	b = ''.join(random.choice(a)for i in range(22))
	
	cv = types.InlineKeyboardButton('Your Info  🎭', url=f'https://t.me/d_xiimbot?info=der{b}{ig}')
	
	xk = types.InlineKeyboardMarkup(row_width=1)
	
	xk.add(cv)
	
	bot.send_message(mo.chat.id,text=f'''<strong>
❖ - Your Id 🎭

|⌯| Id ⌯ </strong><code>{ig}</code>
<strong><s>touch to cope</s></strong>
''', parse_mode='html')

@bot.message_handler(commands=['info', 'photo'])

def send_user_info(message):
    
    user = message.chat
    
    user_info = bot.get_chat(user.id)
    
    first_name = user.first_name 
    
    last_name = message.from_user.full_name
    
    username = user.username 
    
    user_idnc = user.id
    
    bio = user_info.bio
    
    photos = bot.get_user_profile_photos(user_idnc).photos
    
    photo_file_id = None
    
    if photos:
        
        photo_file_id = photos[0][-1].file_id
    
    dev = types.InlineKeyboardButton('pro 👨‍💻', url='t.me/d_xiim')
    
    bb = types.InlineKeyboardMarkup(row_width=1);bb.add(dev)
    
    bot.send_photo(chat_id=message.chat.id, photo=photo_file_id, caption=f'''<strong>
❖ - Your Info 🎭

[⌯] Name ⌯ </strong>{last_name}
<strong>[⌯] User ⌯ </strong>@{username}
<strong>[⌯] Id ⌯ <code>{user_idnc}</code>
[⌯] Bio ⌯ </strong>{bio}
    ''', parse_mode='html', reply_markup=bb)


    
@bot.message_handler(commands=['read', 'r'])

def raddd(re):
		
	with open('banid.txt', "r") as yyy:
			
		yyy.read()
			
		yyy.readline()
			
		yyy.readlines()
			
	with open('sh.txt', "r") as pe:
			
		pe.read()
			
		pe.readline()
			
		pe.readlines()
			
		with open('userss.txt', "r") as kd:
				
			kd.read()
				
			kd.readline()
				
			kd.readlines()
			
		with open('vip.txt', "r") as jk:
			
			jk.read()
			
			jk.readline()
			
			jk.readlines()
			
		bot.send_message(re.chat.id,text='تم إعادة قرائه الملفات')
		
@bot.message_handler(commands=['start'])

def start(m):
	
	if bot.get_chat_member(f"@course_py",m.from_user.id).status == "left":
		
		den = types.InlineKeyboardButton('my channel', url='t.me/course_py')
		
		ka = types.InlineKeyboardButton('bot channel', url='t.me/botatkom')
		
		kc = types.InlineKeyboardMarkup(row_width=2);kc.add(den, ka)
		
		bot.send_message(m.chat.id,f'''<strong>
عذرا عزيزي 📛
عليك الاشتراك بقناة المطور و قناة البوت فضلا
ليصلك كل جديد✨
</strong>
		''', parse_mode='html', reply_markup=kc)
		
		return
		
	elif bot.get_chat_member(f"@botatkom",m.from_user.id).status == "left":
		
		den = types.InlineKeyboardButton('my channel', url='t.me/course_py')
		
		ka = types.InlineKeyboardButton('bot channel', url='t.me/botatkom')
		
		kc = types.InlineKeyboardMarkup(row_width=2);kc.add(den, ka)
		
		bot.send_message(m.chat.id,f'''<strong>
عذرا عزيزي 📛
عليك الاشتراك بقناة المطور و قناة البوت فضلا
ليصلك كل جديد✨
</strong>
		''', parse_mode='html', reply_markup=kc)
		
		return
		
	else:
		
		pass
	
	userss = open('userss.txt', "r").read()
	
	na = m.from_user.full_name
	
	p = m.from_user.id
	
	if str(p) in userss:
		
		pass
		
	else:
		
		with open('userss.txt', "a") as ks:
			
			ks.write(f'{p}\n')
			
	with open('banid.txt', "r") as bd:
			
		banid = bd.read()
		
		if str(p) in banid:
				
			bot.send_message(m.chat.id,text='انت محظور')
				
		else:
			
			with open('sh.txt', "r") as ss:
				
				sh = ss.read()
				
			if not str(p) in sh:
							
					hks = types.InlineKeyboardButton(' develover   ϟ ', url='t.me/d_xiim')
							
					mon = types.InlineKeyboardButton('أسعار الاشتراك 💲', callback_data='mon')
							
					pse = types.InlineKeyboardMarkup(row_width=1);pse.add(mon, hks)
							
					bot.send_message(m.chat.id,text='''
					<strong>
عذرا عزيزي📛🤖

هذه البوت مدفوع قُم بمراسله المطور لتفعيل الاشتراك
</strong>









''', parse_mode='html', reply_markup=pse)
							
			else:
								
				b1 = types.InlineKeyboardButton('👾 gmail 👾', callback_data='b1')
				
				b2 = types.InlineKeyboardButton('👾 yahoo 👾', callback_data='b2')
				
				b3 = types.InlineKeyboardButton('👾 hotmail 👾', callback_data='b3')
				
				b4 = types.InlineKeyboardButton('👾 mail.ru 👾', callback_data='b4')
				
				v = types.InlineKeyboardButton('👾 all domen 👾', callback_data='v')
				
				js = types.InlineKeyboardMarkup(row_width=2);js.add(b1,b2,b3,b4,v)
				
				bot.send_message(m.chat.id,text=f'''<strong>
اهلا بك {na} ،
البوت مخصص لصيد حسابات انستقرام عن طريق لسته✨
اخِتر القسم ثم ارسل لسته تحتوي على الدومين نفسه فضلا🖤</strong>''', parse_mode='html', reply_markup=js)
							
@bot.callback_query_handler(func=lambda call:True)

def call1(call):
	
	if call.data == 'mon':
		
		mn = types.InlineKeyboardButton('develover   ϟ', url='t.me/d_xiim')
		
		mnn = types.InlineKeyboardButton('بوت تواصل محظورين', url='t.me/d_xiimbbot')
		
		ob = types.InlineKeyboardButton('الغاء ✖️')
		
		ido = types.InlineKeyboardMarkup(row_width=2);ido.add(mn, mnn)
		
		ai = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - اسعار الاشتراك في بوت صيد متاحات

⌯ قسم العادي
  - <s>مميزاته</s> :
    1 - فحص لسته انستقرام موحد (كل دومين يفحص ملف واحد )
    2 - بدون حظر
    3 - فحص دقيق

<s>⌯ أسعار قسم العادي</s>
رصيد $
يوم واحد ≈ 3$
يومين ≈ 5$
اسبوع ≈ 14$
اسبوعين ≈ 25$
شهر ≈ 40$

نقاط مليار°
يوم ≈ 8.000
يومين ≈ 15.000
اسبوع ≈ 40.000
شهر ≈ 120.000

<s>⌯ أسعار قسم vip</s>
رصيد$
يوم ≈ 5$
يومين ≈ 9$
اسبوع ≈ 27$
شهر ≈ 75$

نقاط°
يوم ≈ 12.000
يومين ≈ 20.000
اسبوع ≈ 50.000
شهر ≈ 160.000

أقبل بدل تفعيل بالساعات أو يوم 
مثل حسابات أو مقابل مرتب يكون تفعيل بالساعات حسب المقابل

ملاحظات :
	قسم العادي يفحص كل دومين على حده مثلا gmail يفحص فقط gmail كذلك باقي الأقسام 

قسم vip ترسل ملف أو لسته و يفحص اللسته بكل الدومينات الموجوده مثلا ترسل ملف راح يبدي يفحص جميع الدومينات 
إذا كان متاح gmail يرسل متاح gmail
إذا كان متاح yahoo يرسل متاح ياهو
كذلك باقي الدومينات
يعني ترسل ملف و تكعد الصبح تشوف متاحات من جميع دومينات

للاشتراك تواصل على الخاص او بوت التواصل تحت
</strong>
		''', parse_mode='html', reply_markup=ido)
		
	elif call.data == 'ob':
		
		hks = types.InlineKeyboardButton(' develover   ϟ ', url='t.me/d_xiim')
		
		mon = types.InlineKeyboardButton('أسعار الاشتراك 💲', callback_data='mon')
		
		pse = types.InlineKeyboardMarkup(row_width=1);pse.add(mon, hks)
		
		bot.send_message(call.chat.id,text='''
					<strong>
عذرا عزيزي📛🤖

هذه البوت مدفوع قُم بمراسله المطور لتفعيل الاشتراك
</strong>









''', parse_mode='html', reply_markup=pse)
	elif call.data == 'l3':
		
		ll3 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لتفعيل الاشتراك
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(ll3, ll33)
		
	elif call.data == 'l5':
		
		kb = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لتفعيل اشتراك vip
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(kb, ao)
		
	elif call.data == 'l6':
		
		px = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء تفعيل اشتراك vip
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(px, xp)
		
	elif call.data == 'l1':
		
		vb = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لحظره
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(vb, ub)
		
	elif call.data == 'l2':
		
		kf = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء الحظر
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(kf, sb)
		
	elif call.data == 'l4':
		
		fn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء الاشتراك العادي
</strong>
		''', parse_mode='html')
		
		bot.register_next_step_handler(fn, xnxx)
		
	elif call.data == 'l7':
		
		with open('banid.txt', "r") as yyy:
			
			yyy.read()
				
			yyy.readline()
				
			bbaj = yyy.readlines()
			
			bban = int(len(bbaj))
				
		with open('sh.txt', "r") as pe:
				
			pe.read()
				
			pe.readline()
				
			sshn = pe.readlines()
			
			ssh = str(len(sshn))
				
		with open('userss.txt', "r") as kd:
					
			kd.read()
					
			kd.readline()
						
			uuns = kd.readlines()
			
			uus = str(len(uuns))
		with open('vip.txt', "r") as jk:
				
			vvnp = jk.readlines()
			
			vvip = str(len(vvnp))
			
			jk.read()
			
			jk.readline()
			
		p1 = types.InlineKeyboardButton('قائمه المستخدمين', callback_data='p1')
		
		p2 = types.InlineKeyboardButton('قائمه مشتركين عادي', callback_data='p2')
		
		p3 = types.InlineKeyboardButton('قائمه مشتركين vip', callback_data='p3')
		
		p4 = types.InlineKeyboardButton('قائمه المحظورين', callback_data='p4')
		
		ppp = types.InlineKeyboardButton('رجوع ↩️')
		
		p5 = types.InlineKeyboardMarkup(row_width=4);p5.add(p1,p2,p3,p4, ppp)
		oby = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - الإحصائيات :

|⌯| عدد المستخدمين الكلي : {uus}
|⌯| عدد مشتركين العادي : {ssh}
|⌯| عدد مشتركين vip : {vvip}
|⌯| عدد المحظورين : {bban}
</strong>
		''', parse_mode='html', reply_markup=p5)
		
	elif call.data == 'p1':
		with open('userss.txt', "r") as nd:
			so = nd.read()
		back = types.InlineKeyboardButton('رجوع ↩️')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المستخدمين 
{so}
</strong>
		''', parse_mode='html', reply_markup=n)
	
	elif call.data == 'p2':
		with open('sh.txt', "r") as ci:
			sn= ci.read()
		back = types.InlineKeyboardButton('رجوع ↩️')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المشتركين ; النوع : عادي
{sn}
</strong>
		''', parse_mode='html', reply_markup=n) 
	
	elif call.data == 'p3':
		with open('vip.txt', "r") as xi:
			cb = xi.read()
		back = types.InlineKeyboardButton('رجوع ↩️')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المشتركين ; النوع : vip
{cb}
</strong>
		''', parse_mode='html', reply_markup=n)
	
	elif call.data == 'p4':
		with open('banid.txt', "r") as zx:
			er = zx.read()
		back = types.InlineKeyboardButton('رجوع ↩️')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المحظورين
{er}
</strong>
		''', parse_mode='html', reply_markup=n)
	
	elif call.data == 'back':
		with open('banid.txt', "r") as yyy:
			
			yyy.read()
				
			yyy.readline()
				
			bbaj = yyy.readlines()
			
			bban = int(len(bbaj))
				
		with open('sh.txt', "r") as pe:
				
			pe.read()
				
			pe.readline()
				
			sshn = pe.readlines()
			
			ssh = str(len(sshn))
				
		with open('userss.txt', "r") as kd:
					
			kd.read()
					
			kd.readline()
						
			uuns = kd.readlines()
			
			uus = str(len(uuns))
		with open('vip.txt', "r") as jk:
				
			vvnp = jk.readlines()
			
			vvip = str(len(vvnp))
			
			jk.read()
			
			jk.readline()
			
		p1 = types.InlineKeyboardButton('قائمه المستخدمين', callback_data='p1')
		
		p2 = types.InlineKeyboardButton('قائمه مشتركين عادي', callback_data='p2')
		
		p3 = types.InlineKeyboardButton('قائمه مشتركين vip', callback_data='p3')
		
		p4 = types.InlineKeyboardButton('قائمه المحظورين', callback_data='p4')
		
		ppp = types.InlineKeyboardButton('رجوع ↩️')
		
		p5 = types.InlineKeyboardMarkup(row_width=4);p5.add(p1,p2,p3,p4, ppp)
		oby = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - الإحصائيات :

|⌯| عدد المستخدمين الكلي : {uus}
|⌯| عدد مشتركين العادي : {ssh}
|⌯| عدد مشتركين vip : {vvip}
|⌯| عدد المحظورين : {bban}
</strong>
		''', parse_mode='html', reply_markup=p5)
	elif call.data == 'l8':
		
		obyv = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - هذه القسم في صيانه 🤖🛠️
</strong>
		''', parse_mode='html')
	elif call.data == 'b4':
		vl = types.InlineKeyboardButton('رجوع ✖️', callback_data='vl')
		
		cn = types.InlineKeyboardMarkup(row_width=1);cn.add(vl)
		ail = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل الملف ليتم الفحص ✨🖤
</strong>
		''', parse_mode='html', reply_markup=cn)
		
		bot.register_next_step_handler(ail, ali)
	elif call.data == 'v':
		
		dfl = call.from_user.id
		
		ww = open('vip.txt', "r").read()
		
		if not str(dfl) in ww:
			
			ci = types.InlineKeyboardButton('dev °', url='t.me/d_xiim')
			
			rn = types.InlineKeyboardButton('bot', url='t.me/d_xiimbbot')
			
			jd = types.InlineKeyboardButton('رجوع ✖️', callback_data='jd')
			
			xl = types.InlineKeyboardMarkup(row_width=2)
			
			xl.add(ci,rn,jd)
			
			kq = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - عذرا عزيزي هذه القسم vip راسل المطور لتفعيل الاشتراك
</strong>
		''', parse_mode='html', reply_markup=xl)
		
		else:
				
				il = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل الملف ليتم الفحص ✨🖤
</strong>
		''', parse_mode='html')
		
				bot.register_next_step_handler(il, rm)
@bot.message_handler(commands=['admen', 'admn', 'a', 'ad', 'adm'])

def fo(ass):
	
	lol = ass.from_user.id
	
	#@d_xiim - 5903160198 
	#@zskkaf - 6019145503
	if lol == 5903160198 or lol == 6019145503:
		
		l1 = types.InlineKeyboardButton('حظر عضو', callback_data='l1') ####
		
		l2 = types.InlineKeyboardButton('إلغاء حظر عضو', callback_data='l2') ####
		
		l3 = types.InlineKeyboardButton('تفعيل اشتراك( عادي )', callback_data='l3') ####
		
		l4 = types.InlineKeyboardButton('إلغاء تفعيل اشتراك ( عادي )', callback_data='l4') ####
		
		l5 = types.InlineKeyboardButton('تفعيل اشتراك ( vip )', callback_data='l5') ####
		
		l6 = types.InlineKeyboardButton('إلغاء تفعيل اشتراك ( vip )', callback_data='l6') ####
		
		l7 = types.InlineKeyboardButton('الإحصائيات', callback_data='l7') ####
		
		l8 = types.InlineKeyboardButton('الاذاعه', callback_data='l8') ####
		
		lll = types.InlineKeyboardMarkup(row_width=2)
		
		lll.add(l2,l1,l4,l3,l6,l5,l7,l8)
		
		bot.send_message(ass.chat.id,text='اهلا مطوري👨‍💻🖤', reply_markup=lll)
		
	else:
		
		pass
		
def ll33(di):
	
	idsh = di.text
	
	with open('sh.txt', "a") as je:
		
		je.write(f'{idsh}\n')
		
	bot.send_message(di.chat.id,text='تم تفعيل اشتراك اضغط /r  أو /start')
	
def ao(hl):
	try:
		idv = int(hl.text)
	except:
		bot.send_message(hl.chat.id,text='ايدي غير صالح')
	with open('vip.txt', "a") as jje:
		
		jje.write(f'{idv}\n')
		
	bot.send_message(hl.chat.id,text='تم تفعيل اشتراك اضغط /r  أو /start')
	try:
		kag = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idv}&text=تم تفعيل اشتراك اضغط /start او /read")
	except:
		bot.send_message(hl.chat.id, text='لم يتم اعلام المستخدم بأنه تم تفعيل الاشتراك vip')
def ub(iw):
	
	idnv = iw.text
	
	with open('banid.txt', "a") as lje:
		
		lje.write(f'{idnv}\n')
		
	bot.send_message(iw.chat.id,text='تم حظر العضو بنجاح')
	
	try:
		
		kg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idnv}&text=تم حظرك من البوت")
		
	except:
		
		bot.send_message(iw.chat.id,text='تم حظر العضو ولكن يم يتم ارسال رساله له')


def so(ol):
	
	try:
		
		user_id = int(ol.text)
		
	except:
		
		bot.send_message(ol.chat.id,text='ارسل ايدي صالح ')
		
	filename = 'sh.txt'
	
	with open(filename, 'r') as f:
		
		lines = f.readlines()
	
	with open(filename, 'w') as f:
		
		for line in lines:
		   		
		   		if str(user_id) in line:
		   			
		   			continue
		   			
		   		f.write(line)
		   		
	bot.send_message(ol.chat.id,text=f'''<strong>
تم الغاء تفعيل اشتراك العضو : {user_id}
نوع الاشتراك : عادي
</strong>
	''', parse_mode='html')
	
	try:
		
		vw = requests.post(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text=
لقد انتهى تفعيل الاشتراك
نوع الاشتراك : عادي""")

	except:
		
		bot.send_message(ol.chat.id,text='خطا في إرسال للعضو')
		
def sb(bs):
	
	try:
		
		user_id = int(bs.text)
		
	except:
		
		bot.send_message(bs.chat.id,text='ارسل ايدي صالح ')
		
	filename = 'banid.txt'
	
	try:
		
		with open(filename, 'r') as f:
			
			lines = f.readlines()
		
		with open(filename, 'w') as f:
			
			for line in lines:
			   		
			   		if str(user_id) in line:
			   			
			   			continue
			   			
			   		f.write(line)
			   		
	except:
		
		bot.send_message(bs.chat.id,text='هذه العضو غير محظور')
		   		
	try:
		
		khg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text=تم الغاء حظرك اضغط /start")
		
		bot.send_message(bs.chat.id,text='تم الغاء حظر العضو')
		
	except:
		
		bot.send_message(bs.chat.id,text='تم الغاء حظر العضو ولكن لم يستلم رساله الالغاء')

def xp(xx):
	
	try:
		
		user_i= int(xx.text)
		
	except TypeError:
		
		bot.send_message(xx.chat.id,text='ارسل ايدي صالح ')
		
	except IndexError:
		
		bot.send_message(xx.chat.id,text='ارسل ايدي صالح ')
		
	except IndentationError:
		
		bot.send_message(xx.chat.id,text='ارسل ايدي صالح ')
		
	filename = 'vip.txt'
	
	with open(filename, 'r') as f:
		
		lines = f.readlines()
	
	with open(filename, 'w') as f:
		
		for line in lines:
		   		
		   		if str(user_i) in line:
		   			
		   			continue
		   			
		   		f.write(line)
		   		
	try:
		
		bot.send_message(xx.chat.id,text=f'''<strong>
تم الغاء تفعيل اشتراك العضو : {user_i}
نوع الاشتراك : vip
</strong>
	''', parse_mode='html')
	
	except:
		
		pass
		
	try:
		vw = requests.post(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id={user_i}&text=
لقد انتهى تفعيل الاشتراك
نوع الاشتراك : vip""")
	except:
		bot.send_message(xx.chat.id,text='خطا في إرسال للعضو') 
import time

@bot.message_handler(content_types=['document'])
def rm(message):
	try:
		filename = message.document.file_name
		fil = bot.get_file(message.document.file_id)
		dow = bot.download_file(fil.file_path)
		with open(filename, 'wb') as f0:
			f0.write(dow)
		p_file = open(filename, "r")
	except:
		bot.send_message(message.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
		''')
		return
	while True:
		s = p_file.readline().split('\n')[0]
		try:
			email = s.split('@')[0]
		except:
			email = s
		
def ali(z):
 gma = 0
 bma = 0
 ama = 0
 ema = 0
 allma = 0
 bad_p = 0
 try:
  filename = z.document.file_name
  fil = bot.get_file(z.document.file_id)
  dow = bot.download_file(fil.file_path)
  with open(filename, 'wb') as f0:
   f0.write(dow)
  p_file = open(filename, "r")
  mssg=bot.send_message(z.chat.id,text="wait a litele...")
  time.sleep(1)
 except:
  bot.send_message(z.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
  return
 while True:
  s = p_file.readline().split('\n')[0]
  try:
   emai = s.split('@')[0]
   email = f'{emai}@mail.ru'
  except:
   emai = s
   email = f'{emai}@mail.ru'
  url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
  headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
    'content-length': '61',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': str(generate_user_agent()),
    'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0Plwj5(om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
    'x-instagram-ajax': '72bda6b1d047',
    'x-requested-with': 'XMLHttpRequest'
   }
  data = {
    'email' : str(email),
    'username': str(email),
    'first_name': 'my god',
    'opt_into_one_tap': 'false'
   }
  req = requests.post(url, headers=headers, data=data).text
  if "Another account is using the same email." in req:
   gma +=1
   allma +=1
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
   data = {'email': email}
   res= requests.post('https://account.mail.ru/api/v1/user/exists', headers=headers, data=data, timeout=5)
   if '"body":{"exists":true,' in res.text:
    ama +=1
    allma +=1
   elif '"body":{"exists":false,' in res.text:
    ema +=1
    allma +=1
    bot.send_message(z.chat.id,text=f'email : {email}')
   else:
    bad_p +=1
    allma +=1
  else:
   bma +=1
   allma +=1
  with open(filename, 'r') as dc:
   allline = dc.readlines()
   all_line = len(allline)
  ma1 = types.InlineKeyboardButton('Good Insta ►', callback_data='ma1')
  ma2 = types.InlineKeyboardButton(f'{gma}', callback_data='ma2')
  ma3 = types.InlineKeyboardButton('Bad Insta ►', callback_data='ma3')
  ma4 = types.InlineKeyboardButton(f'{bma}', callback_data='ma4')
  ma5 = types.InlineKeyboardButton('Error mail.ru ►', callback_data='ma5')
  ma6 = types.InlineKeyboardButton(f'{bad_p}', callback_data='ma6')
  ma7 = types.InlineKeyboardButton('Bad mail.ru ►', callback_data='ma7')
  ma8 = types.InlineKeyboardButton(f'{ama}', callback_data='ma8')
  ma9 = types.InlineKeyboardButton('Good mail.ru ►', callback_data='ma9')
  ma10 = types.InlineKeyboardButton(f'{ema}', callback_data='ma10')
  maname = types.InlineKeyboardButton(f'{filename}', callback_data='maname')
  maall = types.InlineKeyboardButton(f'{all_line}/{allma}', callback_data='maall')
  maemail = types.InlineKeyboardButton(f'{email}', callback_data='maemail')
  mamar = types.InlineKeyboardMarkup(row_width=2)
  mamar.add(ma9,ma10,ma1,ma2,ma3,ma4,ma5,ma6,ma7,ma8,maname,maall,maemail)
  bot.edit_message_text(chat_id=z.chat.id,message_id=mssg.message_id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : mail.ru</s>
</strong>
   ''',parse_mode='html', reply_markup=mamar)
def xnxx(xn):
	pass
while True:
	def deer():
		try:
			bot.polling(none_stop=True)
		except:
			deer()
	deer()
deer()
