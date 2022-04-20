import os
import telebot
import pymysql as pymysql

#API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot("5398344204:AAFrV9FcGtWC1--ET_TNrRleoNW97QTU4Ys")
accounts = 'https://t.me/proxy?server=20.27.54.191&port=443&secret=ee46bd149ee434573750653180dc729c4e6b796f746f2d752e61632e6a70'

def isUser(id):
    conn = pymysql.connect(host='107.172.21.104', port=3306, user='cn', passwd='86pni6dEtxfRT5MY', db='cn', charset='utf8')
    cur = conn.cursor()
    sql = "select plan_id from v2_user where telegram_id = "+id
    try:
        cur.execute(sql)
        data = cur.fetchall()
        plan_id = data[0][0]
        print(plan_id)
        print(data)
        if plan_id > 0 and plan_id < 4:
            return accounts
        else:
            return False
    except Exception as e:
        return "您未在网站上进行绑定"
    finally:
        conn.close()



@bot.message_handler(content_types=['text'])
def send_texts(message):
  print(str(message.chat.id))
  res = isUser(str(message.chat.id))
  print("判断是不是付费用户:"+res)
  bot.reply_to(message,res)
#1989905589
bot.polling()
