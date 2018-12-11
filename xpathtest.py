import requests
from lxml import etree

url = r'C:\Users\liuchang\Desktop\changoal.html'

with open(url, 'r', encoding='utf-8') as f:
    selector = etree.HTML(f.read())
    # print(selector.xpath('//a/text()'))
    # print(selector.xpath('//title/text()'))
    # print(
    #     selector.xpath(
    #         '/html/body/section/div/div/div[2]/div[1]/div/div[1]/a/text()'))
    print(
        selector.xpath(
            # '/html/body/section/div/div/div[1]/div[1]/div[1]/a/img/@src'))
            '//div[@class="card-image"]/a/img/@src'))
    #/html/body/section/div/div/div[1]/div[1]/div[1]/a/img
    # datas = selector.xpath(
    #     '/html/body/section/div/div/div[2]/div[1]/div/div[1]/a/text()')
    # datas = selector.xpath('//a/text()')
    # datas = [i.strip() for i in datas]
    # datas = [i for i in datas if len(i) > 0]
    # print(datas)
