import grequests
from bs4 import BeautifulSoup
import time

start_time=time.time()

links = [f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}' for page in range(1,4)]
#print(links) 建立網址清單

reqs = (grequests.get(link) for link in links)
resps = grequests.imap(reqs,grequests.Pool(3))

#print(links) 建立請求物件

for index, resp in enumerate(resps):
    soup = BeautifulSoup(resp.text, 'lxml') 
    titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})
    #print(titles) 透過Beautifulsoup取得網頁內容 透過Find all 找出所有標籤下的值

    title_list=[]
    for title in titles:
        title_list.append(title.getText())

#     #print(title_list) 將所有網址的新聞Title放到list 裡面

    urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})

    sub_links =[url.get('href') for url in urls]
    sub_reqs = (grequests.get(sub_link) for sub_link in sub_links)
    sub_resps = grequests.imap(sub_reqs,grequests.Pool(10))

    tag_list=[]
    for sub_resp in sub_resps:
        #print(title_list) 將所有網址的新聞網址找出來
        sub_soup = BeautifulSoup(sub_resp.text, 'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
        for tag in tags:
            tag_list.append(tag.find('a').getText())
            # 將所有網址新聞的附屬Title列出來
    
    print(f"第{index+1}頁")
    print(title_list)
    print(tag_list)

End_time=time.time()
print(f"花費{End_time - start_time}秒")
