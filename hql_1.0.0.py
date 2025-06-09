# coding=utf-8
def md5(input_string):
    """计算MD5哈希值"""
    return hashlib.md5(input_string.encode()).hexdigest()

def rc4_decrypt(key, data):
    """使用RC4算法解密数据"""
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = (S[j], S[i])
    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = (S[j], S[i])
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)

def rc4_encrypt(key, data):
    """使用RC4算法加密数据"""
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = (S[j], S[i])
    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = (S[j], S[i])
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)
if __name__!= '__main__':
    print('？\n？\n？\n？\n？\n？\n？\n？\n？\n？\n')
    exit()
import subprocess
import sys
import os

def check_lib(libname: str, install_name: str=None):
    """\n    检查库是否存在, 不存在则尝试安装\n\n    @ param libname str 库名\n    @ param install_name str 安装名, 默认为库名\n    """
    try:
        __import__(libname)
    except ImportError:
        install_name = install_name or libname
        print(f'检测到缺失库-{install_name},自动安装中. ')
        cmds = [[sys.executable, '-m', 'pip', 'install', install_name], [sys.executable, '-m', 'pip3', 'install', install_name], ['pip', 'install', install_name], ['pip3', 'install', install_name], ['python', '-m', 'pip', 'install', install_name], ['python3', '-m', 'pip', 'install', install_name]]
        for index, cmd in enumerate(cmds):
            try:
                print(f'启用安装方案{index + 1}')
                subprocess.check_call(cmd)
                print('安装成功.')
                return
            except Exception as e:
                print(f'安装失败. 错误信息: {repr(e)}')
        else:
            for index, cmd in enumerate(cmds):
                try:
                    print(f'启用安装方案{index + 7}')
                    os.system(' '.join(cmd))
                    print('安装成功.')
                    return
                except Exception as e:
                    print(f'安装失败. 错误信息: {repr(e)}')
            else:
                sys.exit(f'缺失库 {repr(install_name)} 安装失败. 请手动安装.')
required_libraries = ['requests', 'psutil', 'httpx','art','tqdm']
for lib in required_libraries:
    check_lib(lib)
print(' 导入依赖中...', end='\r')
import threading
import os
import re
import urllib.request
import webbrowser
import datetime
import random
import time
import zlib
import json
import hashlib
import requests
import asyncio
import httpx
import art
from concurrent.futures import ThreadPoolExecutor, as_completed
from base64 import b32decode, b64decode, b85decode
print(' 导入完成...', end='\r')
start_time = time.time()
bai = '[3m'
hx = '[4m'
red = '[31m'
green = '[32m'
yellow = '[33m'
darkblue = '[34m'
blue = '[36m'
pink = '[35m'
end = '[0m'
PURPLE = '[95m'
CYAN = '[36m'
logo = art.tprint("hql\nshuazan")
art.tprint("hql\nshuazan")
os.system('clear')
art.tprint(f'hql\nshuazan')
print(f'{PURPLE}作者:爱吃猫的鱼{end}')
zz = 0
os.system('clear')
art.tprint("hql\nshuazan")
if zz == '1':
    print(f'{red}卡网已跳转{end}')
    webbrowser.open_new('https://ysc.ymyfak.com/links/FD2E96A6')
    print(red + '已尝试跳转卡网' + end)
else:
    if zz == '2':
        url
        webbrowser.open_new('https://t.me/ZCPF66')
        print(red + '已尝试跳转ZCPF66' + end)
    else:
        if zz == '3':
            webbrowser.open_new('http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=7blQgkpMPmBt1tOO6b9wf3xJMlGFUFA_&authKey=fPqR1VU7HDjEd8EhdWGLB6IVJp9oZzZsQQW2UPyBzN7CMZyjcJpbsrYV5S5oY5j3&noverify=0&group_code=581273718')
            print(red + '已尝试跳转Q群@581273718' + end)
qheaders = {'Host': 'sharechain.qq.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 14; zh-CN; PJE110 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/6.12.5.560 Mobile Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-gpc': '1', 'dnt': '1', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5', 'save-data': 'on', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate'}
try:
    page = requests.get('https://share.weiyun.com/W6lgkCWK', headers=qheaders)
    page.raise_for_status()
    page = page.text
except:
    print(f'{red}网络异常{end}')
    sys.exit()
try:
    _ip1 = requests.get('https://www.ipip.net/ip-js/').text
    _ip1 = re.search('text\\(\'([^\']*)', _ip1).group(1)
    _ip2 = requests.get('http://txt.go.sohu.com/ip/soip').text
    _ip2 = re.search('window\\.sohu_user_ip=\"([^\"]*)', _ip2).group(1)
except Exception as e:
    sys.exit()
ip = _ip1
import requests
import hashlib
import json
import time
import random
import datetime
WEIURL = 'http://wy.llua.cn'
WEIAID = '36648'
WEIKEY = 'qdba539963eb718304c'
RC4KEY = 'm33b2b32d459b34fa4e49d73a375705'
DLCODE = 717
EDITION = '1.0'

def md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash

def rc4_decrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = (S[j], S[i])
    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = (S[j], S[i])
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)

def rc4_encrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = (S[j], S[i])
    i = 0
    j = 0
    result = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = (S[j], S[i])
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)
notice = requests.post(WEIURL + '/api/?id=notice&app=' + WEIAID)
print(f"公告：黄清良2.0.1\n{yellow}      无限循环版{end}")

def Login(kami, ID):
    TIME = int(time.time())
    VALUE = 1 + random.random() * 10 + TIME
    SIGN = md5('kami={}&markcode={}&t={}&{}'.format(kami, ID, TIME, WEIKEY))
    DATA = bytes.hex(rc4_encrypt(RC4KEY, 'kami={}&markcode={}&t={}&sign={}&value={}'.format(kami, ID, TIME, SIGN, VALUE)))
    loginData = requests.get(WEIURL + '/api/?id=kmlogon&app=' + WEIAID + '&data=' + DATA)
    loginJson = json.loads(rc4_decrypt(RC4KEY, bytes.fromhex(loginData.text)))
    if loginJson['code'] == DLCODE:
        if loginJson['check'] == md5('{}{}{}'.format(loginJson['time'], WEIKEY, VALUE)):
            print('登录成功，到期时间：' + datetime.datetime.fromtimestamp(loginJson['msg']['vip']).strftime('%Y-%m-%d %H:%M:%S'))
            return True
        print('校验失败')
        return False
    print(loginJson['msg'])
    return False
import os
import base64
from itertools import cycle
CONFIG_FILE = '黄清凉卡密'
RC4_KEY = 'HLypgpALyuwKy1r'

def get_saved_kami():
    if not os.path.exists('黄清凉卡密'):
        return
    try:
        with open('黄清凉卡密', 'r') as f:
            data = f.read()
            if not data:
                raise ValueError('空配置文件')
            return data
    except Exception as e:
        print(f'配置读取失败: {str(e)}，将删除无效配置')
        try:
            os.remove('黄清凉卡密')
        except:
            pass
        return None

def save_kami(kami):
    data = kami
    try:
        with open('黄清凉卡密', 'w') as f:
            f.write(data)
        return True
    except Exception as e:
        print(f'保存失败: {str(e)}')
        return False

def login_flow():
    saved_kami = get_saved_kami()
    if saved_kami:
        print(f'自动登录成功，卡密: {saved_kami}')
        return saved_kami
    return None

# def verity():
#     while True:
#         while (kami := input('请输入卡密: ')) and Login(kami, 'id'):
#             save_kami(kami)
#             continue
#         print('请输入正确的卡密')
# kami = login_flow()
# if kami:
#     if not Login(kami, 'id'):
#         verity()
#     else:
#         if Login(kami, 'id'):
#             save_kami(kami)
# else:
#     verity()
url = 'https://www.kuaishou.com/graphql'
useragents = ['Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1', 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0', 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0', 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3', 'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0', 'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)', 'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)', 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9', 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a', 'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2']

def getHeader():
    """取随机UA"""
    return random.choice(useragents)

def short_url_recover(link):
    """\n    短链复原(同时也请求)\n    @ param string link 短链，可带文本\n    @ return (string 短链, string 长链)\n    """
    try:
        link = re.search('https?://[^\\s/$.?#].[^\\s]*', link).group(0)
    except:
        print(f'{red}链接错误{end}')
        sys.exit()
    print(f'短链:{link}')
    header = {'User-Agent': getHeader(), 'Origin': re.search('https?://[^/]*', link).group(0), 'Referer': re.search('https?://[^?]*', link).group(0), 'Host': re.search('https?://([^/]*)', link).group(1), 'Connection': 'keep-alive'}
    response = requests.get(link, headers=header, allow_redirects=True, timeout=10)
    return (link, response.url)

def get_expTag(link):
    """\n    爬取expTag\n    @ param string link 视频链接\n    @ return string expTag or None(爬取失败)\n    """
    headers = {'Host': 'www.kuaishou.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'X-Requested-With': 'mark.via', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5'}
    try:
        return re.search('\"expTag\":\"([^\"]*)', requests.get(link, headers=headers).text).group(1).encode().decode('unicode_escape')
    except:
        return None
def get_comment():
    """刷评论"""
    global ok
    global now_time
    cks = import_ck()
    slink = input(f'{yellow}输入作品链接: {end}')
    _, link = short_url_recover(slink)
    videoID = re.search('&photoId=(.*?)&', link).group(1)
    authorID = re.search('&userId=(.*?)&', link).group(1)
    print('作者ID：' + authorID + '\n作品ID：' + videoID)
    comment = input(f'{yellow}输入评论内容：{end}')
    try:
        wgc = requests.post('https://api.pearktrue.cn/api/sensitivewords/', data={'text': comment}).json()
        if wgc['code'] == 200:
            print(f'{red}检测到违规词，请重新输入{end}')
            for w in wgc['data']['detected_words']:
                print(w)
            sys.exit()
    except Exception:
        pass
    blackWords = ['重开', '废物', '傻子', '人机', '乐子']
    if any((blackWord in comment for blackWord in blackWords)):
        print(f'{red}检测到违规词{blackWord}{end}')
        sys.exit()
    _headers = {'Host': 'www.kuaishou.com', 'Accept': '*/*', 'Accept-Language': 'zh-Hans-CN,en-US;q=0.8,ja-CN;q=0.5,zh-CN;q=0.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Referer': 'https://www.kuaishou.com/new-reco', 'content-type': 'application/json', 'Origin': 'https://www.kuaishou.com', 'Sec-GPC': '1', 'Connection': 'keep-alive', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Priority': 'u=4'}
    payload = {'operationName': 'visionAddComment', 'variables': {'photoId': videoID, 'content': comment, 'photoAuthorId': authorID}, 'query': 'mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n'}
    expTag = get_expTag(link)
    if expTag:
        payload['variables']['expTag'] = expTag
        print(f'expTag: {expTag}')
    payload = json.dumps(payload)
    cover_print = input(f'{yellow}是否覆盖输出(y|N): {end}')
    cover_print = '\r' if cover_print.lower() == 'y' else '\n'
    total, now_time, ok = (len(cks), 0, 0)
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def task(ck):
        global ok
        global now_time
        with lock1:
            now_time += 1
        headers = _headers.copy()
        headers['User-Agent'] = getHeader()
        headers['Cookie'] = ck
        try:
            response = requests.post(payload, data=headers, headers=headers, timeout=5)
            response.raise_for_status()
        except requests.exceptions.Timeout as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求超时{end}'
        except Exception as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求异常{end}{repr(e)}'
        try:
            response = response.json()
            if response['data']['visionAddComment']['result'] == 1:
                with lock2:
                    ok += 1
                return f' {ok}/{now_time}/{total}-{green}✔评论成功          {end}'
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
        except:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
    while True:
        try:
            print(f'{red}不推荐使用多线程，建议直接回车{end}')
            max_workers = input(f'{yellow}最大线程数(直接回车默认1): {end}')
            max_workers = 1 if max_workers == '' else int(max_workers)
            break
        except:
            print(f'{red}请输入正确的数字{end}')
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, ck) for ck in cks]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result, end=cover_print)
            except Exception as e:
                print(e)

def get_like():
    """刷赞"""
    global ok
    global now_time
    cks = import_ck()
    slink = input(f'{yellow}输入作品链接: {end}')
    _, link = short_url_recover(slink)
    videoID = re.search('&photoId=(.*?)&', link).group(1)
    authorID = re.search('&userId=(.*?)&', link).group(1)
    print('作者ID：' + authorID + '\n作品ID：' + videoID)
    _headers = {'Host': 'www.kuaishou.com', 'Accept-Language': 'zh-Hans-CN,en-US;q=0.8,ja-CN;q=0.5,zh-CN;q=0.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Referer': 'https://www.kuaishou.com/new-reco', 'Content-Type': 'application/json', 'Sec-GPC': '1', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Priority': 'u=4'}
    payload = {'operationName': 'visionVideoLike', 'variables': {'photoId': videoID, 'photoAuthorId': authorID, 'cancel': 0}, 'query': 'mutation visionVideoLike($photoId: String, $photoAuthorId: String, $cancel: Int, $expTag: String) {\n  visionVideoLike(photoId: $photoId, photoAuthorId: $photoAuthorId, cancel: $cancel, expTag: $expTag) {\n    result\n    __typename\n  }\n}\n'}
    expTag = get_expTag(link)
    if expTag:
        payload['variables']['expTag'] = expTag
        print(f'expTag: {expTag}')
    payload = json.dumps(payload)
    cover_print = input(f'{yellow}是否覆盖输出(y|N): {end}')
    cover_print = '\r' if cover_print.lower() == 'y' else '\n'
    total, now_time, ok = (len(cks), 0, 0)
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def task(ck):
        global ok
        global now_time
        with lock1:
            now_time += 1
        headers = _headers.copy()
        headers['User-Agent'] = getHeader()
        headers['Cookie'] = ck
        try:
            response = requests.post('https://www.kuaishou.com/graphql', data=payload, headers=headers, timeout=5)
            response.raise_for_status()
        except requests.exceptions.Timeout as e:
            return f' {ok}/{now_time}/{total}-{red}❌点赞失败，请求超时{end}'
        except Exception as e:
            return f' {ok}/{now_time}/{total}-{red}❌点赞失败，请求异常{end}{repr(e)}'
        try:
            response = response.json()
            if response['data']['visionVideoLike']['result'] == 1:
                with lock2:
                    ok += 1
                return f' {ok}/{now_time}/{total}-{green}✔点赞成功       {end}'
            if response.get('error_msg') == '点赞已达上限':
                return f' {ok}/{now_time}/{total}-{yellow}⚠️点赞已达上限，无法继续点赞{end}'
            if response.get('error_msg') == '账号已被封禁':
                return f' {ok}/{now_time}/{total}-{red}❌账号已被封禁，无法点赞{end}'
            if response.get('error_msg') == '账号被拉黑':
                return f' {ok}/{now_time}/{total}-{red}❌账号被拉黑，无法点赞{end}'
            if response.get('error_msg') == '登录失效':
                return f' {ok}/{now_time}/{total}-{red}❌登录失效，请重新登录{end}'
            return f' {ok}/{now_time}/{total}-{red}❌点赞失败       {end}'
        except:
            return f' {ok}/{now_time}/{total}-{red}❌点赞失败       {end}'
    while True:
        try:
            print(f'{red}不推荐使用多线程，建议直接回车{end}')
            max_workers = input(f'{yellow}最大线程数(直接回车默认1): {end}')
            max_workers = 1 if max_workers == '' else int(max_workers)
            break
        except:
            print(f'{red}请输入正确的数字{end}')
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, ck) for ck in cks]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result, end=cover_print)
            except Exception as e:
                print(e)

def bad_comment():
    """刷恶评"""
    global ok
    global now_time
    cks = import_ck()
    slink = input(f'{yellow}输入作品链接: {end}')
    _, link = short_url_recover(slink)
    videoID = re.search('&photoId=(.*?)&', link).group(1)
    authorID = re.search('&userId=(.*?)&', link).group(1)
    print('作者ID：' + authorID + '\n作品ID：' + videoID)
    bad_words = ['我是一个黑贵', '冯宝宝and龙可敬', '毕竟我是猪头焖子','你好','我是谢先锋，我是一头猪','黄清亮祝你天天开心','文博天下']
    _headers = {'Host': 'www.kuaishou.com', 'Accept': '*/*', 'Accept-Language': 'zh-Hans-CN,en-US;q=0.8,ja-CN;q=0.5,zh-CN;q=0.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Referer': 'https://www.kuaishou.com/new-reco', 'content-type': 'application/json', 'Origin': 'https://www.kuaishou.com', 'Sec-GPC': '1', 'Connection': 'keep-alive', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Priority': 'u=4'}
    _payload = {'operationName': 'visionAddComment', 'variables': {'photoId': videoID, 'photoAuthorId': authorID, 'content': '', 'replyToCommentId': None, 'replyTo': None, 'expTag': ''}, 'query': 'mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n'}
    expTag = get_expTag(link)
    if expTag:
        _payload['variables']['expTag'] = expTag
        print(f'expTag: {expTag}')
    cover_print = input(f'{yellow}是否覆盖输出(y|N): {end}')
    cover_print = '\r' if cover_print.lower() == 'y' else '\n'
    total, now_time, ok = (100555946, 0, 0)
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def task(ck):
        global ok
        global now_time
        with lock1:
            now_time += 1
        headers = _headers.copy()
        headers['User-Agent'] = getHeader()
        headers['Cookie'] = ck
        payload = _payload.copy()
        payload['variables']['content'] = random.choice(bad_words)
        payload = json.dumps(payload)
        try:
            response = requests.post('https://www.kuaishou.com/graphql', data=payload, headers=headers, timeout=5)
            response.raise_for_status()
        except requests.exceptions.Timeout as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求超时{end}'
        except Exception as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求异常{end}{repr(e)}'
        try:
            response = response.json()
            if response['data']['visionAddComment']['result'] == 1:
                with lock2:
                    ok += 1
                return f' {ok}/{now_time}/{total}-{green}✔评论成功        {end}'
            if response.get('error_msg') == '评论已达上限':
                return f' {ok}/{now_time}/{total}-{yellow}⚠️评论已达上限，无法继续评论{end}'
            if response.get('error_msg') == '账号已被封禁':
                return f' {ok}/{now_time}/{total}-{red}❌账号已被封禁，无法评论{end}'
            if response.get('error_msg') == '账号被拉黑':
                return f' {ok}/{now_time}/{total}-{red}❌账号被拉黑，无法评论{end}'
            if response.get('error_msg') == '登录失效':
                return f' {ok}/{now_time}/{total}-{red}❌登录失效，请重新登录{end}'
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
        except:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
    while True:
        try:
            print(f'{red}不推荐使用多线程，建议直接回车{end}')
            max_workers = input(f'{yellow}最大线程数(直接回车默认1): {end}')
            max_workers = 1 if max_workers == '' else int(max_workers)
            break
        except:
            print(f'{red}请输入正确的数字{end}')
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, ck) for ck in cks]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result, end=cover_print)
            except Exception as e:
                print(e)
    def task(ck):
        global ok
        global now_time
        with lock1:
            now_time += 1
        headers = _headers.copy()
        headers['User-Agent'] = getHeader()
        headers['Cookie'] = ck
        payload = _payload.copy()
        payload['variables']['content'] = random.choice(bad_words)
        payload = json.dumps(payload)
        try:
            response = requests.post('https://www.kuaishou.com/graphql', data=payload, headers=headers, timeout=5)
            response.raise_for_status()
        except requests.exceptions.Timeout as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求超时{end}'
        except Exception as e:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败，请求异常{end}{repr(e)}'
        try:
            response = response.json()
            if response['data']['visionAddComment']['result'] == 1:
                with lock2:
                    ok += 1
                return f' {ok}/{now_time}/{total}-{green}✔评论成功        {end}'
            if response.get('error_msg') == '评论已达上限':
                return f' {ok}/{now_time}/{total}-{yellow}⚠️评论已达上限，无法继续评论{end}'
            if response.get('error_msg') == '账号已被封禁':
                return f' {ok}/{now_time}/{total}-{red}❌账号已被封禁，无法评论{end}'
            if response.get('error_msg') == '账号被拉黑':
                return f' {ok}/{now_time}/{total}-{red}❌账号被拉黑，无法评论{end}'
            if response.get('error_msg') == '登录失效':
                return f' {ok}/{now_time}/{total}-{red}❌登录失效，请重新登录{end}'
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
        except:
            return f' {ok}/{now_time}/{total}-{red}❌评论失败         {end}'
    while True:
        try:
            print(f'{red}不推荐使用多线程，建议直接回车{end}')
            max_workers = input(f'{yellow}最大线程数(直接回车默认1): {end}')
            max_workers = 1 if max_workers == '' else int(max_workers)
            break
        except:
            print(f'{red}请输入正确的数字{end}')
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, ck) for ck in cks]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result, end=cover_print)
            except Exception as e:
                print(e)
    while True:
        try:
            print(f'{red}不推荐使用多线程，建议直接回车{end}')
            max_workers = input(f'{yellow}最大线程数(直接回车默认1): {end}')
            max_workers = 1 if max_workers == '' else int(max_workers)
            break
        except:
            print(f'{red}请输入正确的数字{end}')
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task, ck) for ck in cks]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result, end=cover_print)
            except Exception as e:
                print(e)
def get_content(phone, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'请求发生错误：{e}')

def main_menu8():
    import requests
    import webbrowser
    print(green + '作者QQ1730399424' + red)

    def main():
        try:
            print('请使用最新复制的链接，防止解析失败')
            lj = input('输入作品链接:')
            response = requests.get('https://api.kxzjoker.cn/API/jiexi_video.php?url=' + lj)
            response.raise_for_status()
            data = response.json()
            if data.get('success'):
                video_title = data.get('data', {}).get('video_title', '未知文案')
                video_url = data.get('data', {}).get('video_url', '未知视频链接')
                image_url = data.get('data', {}).get('image_url', '未知封面链接')
                print(f'文案：{video_title}')
                print(f'视频链接：{video_url}')
                print(f'封面链接：{image_url}')
                川川 = ''.join([i.strip('') for i in video_url])
                川川i = ''.join([i.strip('') for i in video_url])
                print(川川)
                zz = input('输入[1]跳转视频链接/[2]跳转封面链接')
                if zz == '1':
                    url = video_url
                    webbrowser.open_new(url)
                else:
                    if zz == '2':
                        url = image_url
                        webbrowser.open_new(url)
                return (video_title, video_url, image_url)
            print('解析失败：', data.get('message'))
            return (None, None, None)
        except requests.RequestException as e:
            print(f'请求失败：{e}')
            return (None, None, None)
    if __name__ == '__main__':
        main()

def get_ck_list(jk):
    try:
        ck_list = requests.get(jk, timeout=30)
        ck_list.raise_for_status()
    except Exception as e:
        print(f'{red}请求错误{repr(e)}，如果是第一次使用，请重新运行。否则联系作者{end}')
        sys.exit()
    if ck_list.text!= '文件不存在':
        ck_list = ck_list.text.splitlines()
        if not ck_list[len(ck_list) - 1]:
            ck_list.pop(len(ck_list) - 1)
        os.system('clear')
        art.tprint("hpl\nshuazan")
        print(yellow + f'导入成功，接口数量: {len(ck_list)}' + end)
        return ck_list
    print(f'{red}ck异常{end}')
    sys.exit()

def import_ck():
    """导入cookie"""
    ck_count = re.search('接口数量【(.*?)】', page).group(1)
    print(red + f'接口数量:线路1:150/线路2/390' + end)
    print(f'{yellow}[1] 线路一\n{blue}[2] 线路二{end}')
    while True:
        xl = input(f'{yellow}请选择线路:{end}')
        if xl in [str(i + 1) for i in range(5)]:
            break
        print(f'{red}请输入正确的选择{end}')
    if xl in [str(i + 1) for i in range(5)]:
        jk = re.search(f'接口链接{xl}【(https?://[^\\s/$.?#].[^\\s]*)】', page).group(1)
        return get_ck_list(jk)
    sys.exit('?川川')
def _getHeader(target_url: str, useAndroid: bool=False):
    if useAndroid:
        UA = 'Mozilla/5.0 (Linux; U; Android 14; zh-CN; PJE110 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/6.12.5.560 Mobile Safari/537.36'
    else:
        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
    headers = {'User-Agent': UA, 'Host': re.search('https?://([^/]*)', target_url).group(1), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Connection': 'keep-alive', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': re.search('https?://([^/]*)', target_url).group(0)}
    return headers
funcs = [get_comment, get_like, bad_comment,main_menu8]
print(' 导入主程序中...', end='\r')
import threading
import os
import re
import urllib.request
import webbrowser
import datetime
import random
import time
import zlib
import json
import hashlib
import requests
import asyncio
import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed
from base64 import b32decode, b64decode, b85decode
time.sleep(0.7)
print(' 导入完成...', end='\r')
print(f"\033[1;33;40m\n@爱吃猫的鱼制作,黄清凉刷取程序,未经作者允许禁止转载!\033[0m")
print(f"\033[1;32;40m========================main========================\033[m")
qw = random.randint(1,10)
def key(myao):
    i = 6
    while True:
        a = input("请输入密钥进行解密:")
        if a == myao:
            print("\033[1;32;40m密钥正确!\033[0m")
            break
        else:
            i -= 1
            print(f"\033[1;31;40m请重新输入,输入错误!你还有{i}次机会!\033[0m")
        if i <= 0:
            print("机会已用完,程序强制退出!")
            exit()
def main():
    while True:
            print(r" _             _")
            print(r"| |__    __ _ | |")
            print(r"| '_ \  / _` || |")
            print(r"| | | || (_| || |")
            print(r"|_| |_| \__, ||_|")
            print(r"           |_|")                  
            print(r"      _")
            print(r" ___ | |__   _   _   __ _  ____  __ _  _ __")
            print(r"/ __||  _ \ | | | | / _  ||_  / / _  ||  _ \"")
            print(r"\__ \| | | || |_| || (_| | / / | (_| || | | |")
            print(r"|___/|_| |_| \__,_| \__,_|/___| \__,_||_| |_|")
            print("欢迎使用黄清凉刷取工具!")
            print(f"\033[31ctrl + c强制退出{end}")
            print("\033[33m[1] 刷赞")
            print("\033[34m[2] 刷评论")
            print("\033[35m[3] 刷流量")
            break
    li = ["1","2","3"]
    while True:
        time.sleep(0.5)
        a = input("\033[31m请选择你想要使用的操作(1,2,3)：\033[0m")
        if a in li and a == "3" and a.isdigit():
            print(f"\033[1;30;40m你选择了选项{a},但功能正在制作中...\033[0m")
        elif a in li and a == "1" and a.isdigit():
                qe = random.randint(10,25)
                print("\r\033[1;32;40m\r==========刷赞初始化==========\033[0m")
                get_like()
        elif a in li and a == "2" and a.isdigit():
                print(f"{green}\r==========评论初始化=========={end}")
                bad_comment()
        elif a not in li:
                print("目标不存在")
key("qwerty")
main()








