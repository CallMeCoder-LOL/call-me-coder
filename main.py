import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from dato import dato
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '8031549285:AAFfbgMMJMIDyeB9JyIFXl_-TvBRHV_exII'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=1815616383 
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='FREE'
			with open("data.json", "r", encoding="utf-8") as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "FREE",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w', encoding='utf-8') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == 'FREE':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/bkddgfsa/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/bkddgfsa/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='FREE'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵 ✅
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 

𝟯𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 ✅
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='FREE'
		if BL == 'FREE':
			with open("data.json", "r", encoding="utf-8") as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "FREE",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w', encoding='utf-8') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r', encoding='utf-8') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = 'FREE'
			with open("data.json", "w", encoding="utf-8") as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛️",callback_data='br')
		contact_buttonn = types.InlineKeyboardButton(text=f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛️ 𝟮",callback_data='brr')
		sw = types.InlineKeyboardButton(text=f"𝙋𝙖𝙨𝙨𝙚𝙙",callback_data='passed')
		sd = types.InlineKeyboardButton(text=f"𝙋𝙖𝙨𝙨𝙚𝙙 𝟮",callback_data='passet')
		sg = types.InlineKeyboardButton(text=f"𝙋𝙖𝙨𝙨𝙚𝙙 𝟯",callback_data='passeg')
		sa = types.InlineKeyboardButton(text=f"𝙋𝙖𝙨𝙨𝙚𝙙 𝟰",callback_data='passeh')
		saw = types.InlineKeyboardButton(text=f"𝙋𝙖𝙨𝙨𝙚𝙙 (𝑨𝑳𝑳)",callback_data='passeds')
		stripe1 = types.InlineKeyboardButton(text=f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛",callback_data='stripeauth1')
		stripe2 = types.InlineKeyboardButton(text=f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 𝟮",callback_data='stripeauth2')
		braincharge = types.InlineKeyboardButton(text=f"𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$",callback_data='charge')
		newcharge = types.InlineKeyboardButton(text=f"𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟮$",callback_data='newchargee')
		newcharg = types.InlineKeyboardButton(text=f"𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$ 𝟮",callback_data='newchargeee')
		keyboard.add(contact_button)
		keyboard.add(contact_buttonn)
		keyboard.add(sw)
		keyboard.add(sd)
		keyboard.add(sg)
		keyboard.add(sa)
		keyboard.add(saw)
		keyboard.add(stripe1)
		keyboard.add(stripe2)
		keyboard.add(braincharge)
		keyboard.add(newcharge)
		keyboard.add(newcharg)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘼𝙪𝙩𝙝'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='Risk'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}	
	
{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(25)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'brr')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘼𝙪𝙩𝙝 𝟮'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(idkhoww(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='Risk'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}

{str(dato(cc[:6]))}		

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(25)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'passed')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝙋𝙖𝙨𝙨𝙚𝙙'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(passed(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝙖𝙨𝙨𝙚𝙙 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'passeds')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝙋𝙖𝙨𝙨𝙚𝙙 (𝑨𝑳𝑳)'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					start_time = time.time()
					try:
						functions_dict = {
						    #otp: "𝙋𝙖𝙨𝙨𝙚𝙙 𝟰",
						    vnv: "𝙋𝙖𝙨𝙨𝙚𝙙 𝟯",
						    vbb: "𝙋𝙖𝙨𝙨𝙚𝙙 𝟮",
						    passed: "𝙋𝙖𝙨𝙨𝙚𝙙"
						}
						chosen_func = random.choice(list(functions_dict.keys()))
						last = str(chosen_func(cc))
						display_name = functions_dict[chosen_func]
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					gateway = types.InlineKeyboardButton(f"• 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➜ {display_name} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝙖𝙨𝙨𝙚𝙙 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, gateway, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {display_name}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last or 'Charge 100$' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'passet')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟮'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(vbb(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝙖𝙨𝙨𝙚𝙙 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'passeg')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟯'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(vnv(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝙖𝙨𝙨𝙚𝙙 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'passeh')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟰'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(otp(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝙖𝙨𝙨𝙚𝙙 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'stripeauth1')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(stripeauth(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Your Payment Method Successfully Added." in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'stripeauth2')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 𝟮'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(fuck(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Your Payment Method Successfully Added." in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'charge')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(brchargeeee(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘾𝙝𝙖𝙧𝙜𝙚 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Charge" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'newchargee')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟮$'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(idkhow(cc))
					except Exception as e:
						print(e)
						last = "البروكسى مات"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘾𝙝𝙖𝙧𝙜𝙚 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Charge" in last or 'Charge (OTP)' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'newchargeee')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$ 𝟮'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(idkhowww(cc))
					except Exception as e:
						print(e)
						last = "البروكسى مات"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘾𝙝𝙖𝙧𝙜𝙚 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @baba_coder''', reply_markup=mes)
					
					msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
					if "Charge" in last or 'Charge (OTP)' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(20)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @baba_coder')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(stripeauth(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Your Payment Method Successfully Added." in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.dik') or message.text.lower().startswith('/dik'))
def respond_to_vbv(message):
	gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(brchargeeee(cc))
	except Exception as e:
		last='Errorr'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Charge" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.zip') or message.text.lower().startswith('/zip'))
def respond_to_vbv(message):
	gate='𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟮$'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 20:
			bot.reply_to(message, f"<b>Try again after {20-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(idkhow(cc))
	except Exception as e:
		last='Errorr'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Charge" in last or 'Charge (OTP)' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cos') or message.text.lower().startswith('/cos'))
def respond_to_vbv(message):
	gate='𝘾𝙝𝙖𝙧𝙜𝙚 𝟬.𝟬𝟭$ 𝟮'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 20:
			bot.reply_to(message, f"<b>Try again after {20-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(idkhowww(cc))
	except Exception as e:
		last='Errorr'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘾𝙝𝙖𝙧𝙜𝙚 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Charge" in last or 'Charge (OTP)' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sp') or message.text.lower().startswith('/sp'))
def respond_to_vbv(message):
	gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 𝟮'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(fuck(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Your Payment Method Successfully Added." in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	gate='𝙋𝙖𝙨𝙨𝙚𝙙'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(passed(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbb') or message.text.lower().startswith('/vbb'))
def respond_to_vbv(message):
	gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟮'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 15:
			bot.reply_to(message, f"<b>Try again after {15-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(vbb(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbc') or message.text.lower().startswith('/vbc'))
def respond_to_vbv(message):
	gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟯'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 15:
			bot.reply_to(message, f"<b>Try again after {15-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(vnv(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbx') or message.text.lower().startswith('/vbx'))
def respond_to_vbv(message):
	gate='𝙋𝙖𝙨𝙨𝙚𝙙 𝟰'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 15:
			bot.reply_to(message, f"<b>Try again after {15-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(otp(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "3DS Authenticate Successful" in last or '3DS Authenticate Attempt Successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 25:
			bot.reply_to(message, f"<b>Try again after {25-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chl') or message.text.lower().startswith('/chl'))
def respond_to_vbv(message):
	gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 𝟮'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open("data.json", "r", encoding="utf-8") as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open("data.json", "r", encoding="utf-8") as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "FREE",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='FREE'
	if BL == 'FREE':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r', encoding='utf-8') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
للشراء من هنا @baba_coder </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Baba_Coder")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r', encoding='utf-8') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = 'FREE'
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 25:
			bot.reply_to(message, f"<b>Try again after {25-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(idkhoww(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
[<a href="https://t.me/baba_coder">ϟ</a>] 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		

{str(dato(cc[:6]))}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝘽𝙞𝙣 ➼ {cc[:6]}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}

𝗕𝗼𝘁 𝗕𝘆: @baba_coder</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r', encoding='utf-8') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open("data.json", "w", encoding="utf-8") as file:
				json.dump(json_data, file, indent=2)
			with open("data.json", "r", encoding="utf-8") as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w', encoding='utf-8') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>CODER VIP 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open("data.json", "r", encoding="utf-8") as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='CODER-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='VIP'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open("data.json", "r", encoding="utf-8") as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w', encoding='utf-8') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("Bot Is Running")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"Error Exception : {e}")