import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

try:
    response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt', headers=headers, timeout =5)
        #print (response.text) 取得bbc 財金網址

    if response.status_code ==200:
        soup = BeautifulSoup(response.text, 'lxml') 
        title = soup.find('a',{'class':'bbc-uk8dsi e1d658bg0'})
        #print(titles) 透過Beautifulsoup取得網頁內容 透過Find all 找出所有標籤下的值
        if title:
            result = title.getText()
            print(result)
        else:
            print('元素不存在')
    else:
        print('狀態非200')

except Exception as e:
    print(str(e))