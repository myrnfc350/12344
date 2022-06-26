import requests
import random
import time
import os

from update import gettoken


CONFIG_ID = os.environ['CONFIG_ID']
CONFIG_KEY = os.environ['CONFIG_KEY']
refresh_path = 'refresh.txt'
cnt = 0

url_list = [
    'https://graph.microsoft.com/v1.0/users',
    'https://graph.microsoft.com/v1.0/me/drive',
    'https://graph.microsoft.com/v1.0/drive/root',
    'https://graph.microsoft.com/v1.0/me/drive/root',
    'https://graph.microsoft.com/v1.0/me/drive/recent',
    'https://graph.microsoft.com/v1.0/me/drive/root/search',
    'https://graph.microsoft.com/v1.0/me/drive/sharedWithMe',
    'https://graph.microsoft.com/v1.0/me/drive/root/children',
    'https://graph.microsoft.com/v1.0/me/messages',
    'https://graph.microsoft.com/beta/me/messages',
    'https://graph.microsoft.com/beta/me/findRooms',
    'https://graph.microsoft.com/v1.0/me/mailFolders',
    'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
    'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta',
    # 'https://api.powerbi.com/v1.0/myorg/apps',
    'https://graph.microsoft.com/v1.0/me/outlook/masterCategories'
]


def main():
    with open(refresh_path, 'r') as f:
        headers = {
            'Authorization': gettoken(f.read())['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
        }
    global cnt
    
    print('此次运行开始时间为:', time.asctime(time.localtime(time.time())))
    
    for index in random.sample(range(len(url_list)), len(url_list)):
        try:
            res = requests.get(url_list[index], headers=headers)
            if res.status_code == 200:
                cnt += 1
                print(f"url-{index+1:02d} 共调用成功{cnt}次")
            else:
                print(f"url-{index+1:02d} 调用失败: {res.status_code}")
        except Exception as e:
            print(f"url-{index+1:02d} 调用失败: {e}")
    

if __name__ == "__main__":
    for _ in range(6):
        time.sleep(random.randint(600, 1200))
        main()