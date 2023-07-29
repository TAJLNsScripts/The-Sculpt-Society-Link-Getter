import os
import re
import json
import codecs
import requests
from bs4 import BeautifulSoup

#Config
session = ''

def ascii_clear():
    os.system('cls||clear')
    print("""                                                                                                                                                                       
                                                    
              &&&&&&&&&&&&&&&&&&&&&&              
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&          
       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&       
     &&&&&&&&&&&&&&&         .&&&&&&&&&&&&&&&     
   &&&&&&&&&&&&                   &&&&&&&&&&&&    
  &&&&&&&&&&&                        &&&&&&&&&&&  
 &&&&&&&&&&                           #&&&&&&     
 &&&&&&&&&                             &&&        
,&&&&&&&&&                                        
.&&&&&&&&&                                        
 &&&&&&&&&                      &&&&&&&&          
 &&&&&&&&&&                  &&&&&&&&&&&&&/       
  &&&&&&&&&&&                &&&&&&&&&&&&&&&&     
   /&&&&&&&&&&&&                  &&&&&&&&&&&&    
     &&&&&&&&&&&&&&&&                &&&&&&&&&&/  
       &&&&&&&&&&&&&#                 &&&&&&&&&&  
          &&&&&&&%                     &&&&&&&&&& 
                                        &&&&&&&&& 
                                        &&&&&&&&& 
        &&                             &&&&&&&&&& 
     &&&&&&                           #&&&&&&&&&  
  &&&&&&&&&&&                        &&&&&&&&&&&  
   &&&&&&&&&&&&.                  &&&&&&&&&&&&    
     &&&&&&&&&&&&&&&         (&&&&&&&&&&&&&&&     
       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&       
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&          
              &&&&&&&&&&&&&&&&&&&&&&                                    

                Sculpt link getter
                    TAJLN 2023
""")

def get_auth_token():

    headers = {
        'authority': 'app.thesculptsociety.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get('https://app.thesculptsociety.com/login', headers=headers)
    response.raise_for_status()
    
    r = {}
    
    r['_session'] = response.cookies['_session']
    r['token'] = BeautifulSoup(response.content, 'lxml').find("meta", {"name":"csrf-token"})['content']
    
    return r
    
def do_login(email, password, authenticity_token, session):
    
    data = {
        'email': email,
        'authenticity_token': authenticity_token,
        'utf8': '✓',
        'password': password,
    }
    
    cookies = {
        '_session': session,
    }
    
    headers = {
        'authority': 'app.thesculptsociety.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://app.thesculptsociety.com',
        'pragma': 'no-cache',
        'referer': 'https://app.thesculptsociety.com/login',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.post('https://app.thesculptsociety.com/login', cookies=cookies, headers=headers, data=data)
    response.raise_for_status()
    
    return response.cookies['_session']
    
def logout_all_devices(session):
    cookies = {
        '_session': session,
    }

    headers = {
        'authority': 'app.thesculptsociety.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get('https://app.thesculptsociety.com/logout_all_devices', cookies=cookies, headers=headers)
    response.raise_for_status()
    
def browse_request(session):
    cookies = {
        '_session': session,
    }

    headers = {
        'authority': 'app.thesculptsociety.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://app.thesculptsociety.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get('https://app.thesculptsociety.com/browse', cookies=cookies, headers=headers)
    response.raise_for_status()
    
    return response.cookies['_session']
    
def request_page(page_url, session):
    cookies = {
        '_session': session,
    }

    headers = {
        'authority': 'app.thesculptsociety.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    
    script_tag = str(BeautifulSoup(response.content, 'lxml').findAll('script')[22])
    
    embed_url_match = re.search(r'embed_url:\s*"([^"]+)"', script_tag)
    if embed_url_match:
        return embed_url_match.group(1)
    else:
        ascii_clear()
        print("Embed URL not found.")
        quit()
    
def replace_unicode_escape(match):
    return codecs.decode(match.group(0), 'unicode_escape')    

def request_embed(url):
    headers = {
        'authority': 'embed.vhx.tv',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://app.thesculptsociety.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    
    script_tag = str(BeautifulSoup(response.content, 'lxml').findAll('script')[1])
    
    config_url_match = re.search(r'config_url":"([^"]+)"', script_tag)
    if config_url_match:
        
        pattern = r'\\u[0-9a-fA-F]{4}'
        converted_url = re.sub(pattern, replace_unicode_escape, config_url_match.group(1))
        
        return converted_url
    else:
        print("Config URL not found.")
    
def request_config(url):
    headers = {
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://embed.vhx.tv',
        'Pragma': 'no-cache',
        'Referer': 'https://embed.vhx.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.content
    

   
#auth = get_auth_token()
#authenticity_token = auth['token']
#session = auth['_session']

#email = ''
#password = ''

"""
Login doesn't work, please manually copy and paste the _session cookie into the "session" variable at the top of the file
"""

if session == '':
    ascii_clear()
    print('Session variable is empty, please set it at the top of the file')
    quit()
    

ascii_clear()
url = input('Enter url: ')

embed_url = request_page(url, session)
config_url = request_embed(embed_url)

data = json.loads(request_config(config_url))
progressive = data['request']['files']['progressive']


best_num = 0
for p in progressive:
    if p['height'] > best_num:
        best_num = p['height']
        best_quality = p

ascii_clear()
print('Info:')
print('- Quality: ' + best_quality['quality'])
print('- FPS: ' + str(best_quality['fps']))
print('- Link: ' + best_quality['url'])