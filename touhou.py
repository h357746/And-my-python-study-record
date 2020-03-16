import requests
from lxml import etree
import os
import time
from concurrent import futures
headers = {
    'Referer': 'https://touhou.dorori.ml/post',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
def touhou(src):
    resp = requests.get(src, headers=headers)
    html = etree.HTML(resp.text)
    url=html.xpath('//*[ @ id = "highres"] /@href')[0]
    filename = url.split('/')[-1]
    print(url)
    img = requests.get(url)
    if not os.path.exists('imgs/'):
        os.makedirs('imgs/')
    with open('imgs/{}'.format(filename),'wb') as file:
         file.write(img.content)

def get_page(url):
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    print(resp,url)
    srcs = html.xpath('//*[@id="post-list-posts"]//a[@class="thumb"]/@href')
    ex = futures.ThreadPoolExecutor(max_workers=40)
    for src in srcs:
        src='https://touhou.dorori.ml/'+src
        ex.submit(touhou,src)
    try:
         next_links = 'https://touhou.dorori.ml/'+html.xpath('//*[@id="paginator"]/div/a[@class="nextPage"]/@href')[0]
    except IndexError as e:
         print('没有下一下了！')
         next_links = ''
    return next_links
def main():

    next_link = 'https://touhou.dorori.ml/post?page=1'

    while next_link != '':
        time.sleep(2)
        next_link=get_page(next_link)
        print(next_link)
if __name__ == '__main__':
    main()
