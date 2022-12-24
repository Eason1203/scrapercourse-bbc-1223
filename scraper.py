import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')
#print (response.text) 取得bbc 財金網址

soup = BeautifulSoup(response.text, 'lxml') 
titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})
#print(titles) 透過Beautifulsoup取得網頁內容 透過Find all 找出所有標籤下的值

title_list=[]
for title in titles:
    title_list.append(title.getText())

#print(title_list) 將所有網址的新聞Title放到list 裡面

urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})

tag_list=[]
for url in urls:
    #print(url.get('href'))
    #print(title_list) 將所有網址的新聞網址找出來
    sub_response = requests.get(url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
    for tag in tags:
        tag_list.append(tag.find('a').getText())
         # 將所有網址新聞的附屬Title列出來
print(tag_list)

       
