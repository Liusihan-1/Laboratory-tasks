#!/usr/bin/env python
#coding:utf-8

import csv
import re
import requests
from bs4 import BeautifulSoup

#创造csv文件的表头
header_list = ['房源编号','城市','区','方位','房屋名','大小','租赁方式','朝向','月租','计费方式','几室','几厅','几卫',
               '入住','租期','看房','所在楼层','总楼层','电梯','车位','用水','用电','燃气','采暖']

#UA伪装
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }

with open('贝壳网宝鸡房源.csv', 'w', newline='') as csv_out_file:
    filewriter = csv.writer(csv_out_file)
    filewriter.writerow(header_list)
    for page in range(1, 51):
        # step 1指定url
        url = 'https://baoji.zu.ke.com/zufang/pg'+str(page)+'/#contentList'
        # step 2发送请求
        response = requests.get(url=url, headers=headers)
        # step 3 获取响应数据
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')#一开始我用的是lxml，但现在网页都是html所以也就改成了html.parser

        # -----------------------------属于' <房源列表模块 >'------------------------------
        codes = []  # 存储房源编号的列表
        regions = []  # 存储房源地区的列表
        div_list = soup.find_all(class_='content__list--item')#按照标签爬取需要的数据(地区和编码组成后续url需要的id身份)
        for div in div_list:
            code = re.search(r'data-house_code="(.*?)" ', str(div)).group()[17:-2]#截取=号之后的字符串编码
            codes.append(code)
        p_list = soup.find_all(class_='content__list--item--des')
        for p in p_list:
            a_list = p.find_all('a')
            # print(a_list)得到了含有地区的标签信息
            region = []
            for i in range(len(a_list)):
                a_text = a_list[i].text
                region.append(a_text)
            regions.append(region)#将每所房屋对应的区、方位、小区名分开存储到regions列表

        for i in range(len(codes)):
            information = []  # 存储房源信息的列表
            information.extend([codes[i],'宝鸡'] + regions[i])# must be str,not list
            # step 1指定url
            url = 'https://baoji.zu.ke.com/zufang/' + codes[i] + '.html'
            # step 2发送请求
            response = requests.get(url=url, headers=headers)
            # step 3 获取响应数据
            text = response.text
            soup = BeautifulSoup(text, 'html.parser')
            # -----------------------------属于' <房源标签列表 >'------------------------------
            ul_text = soup.find('ul', class_='content__aside__list').text
            div_text = soup.find('div', class_='content__aside--title').text
            area = re.search(r' (.*?)㎡', ul_text).group()[1:]
            lease = re.search(r'租赁方式：(.*?)\n', ul_text).group()[5:-1]
            direction = re.search(r'朝向楼层：(.*?) ', ul_text).group()[5:-1]
            price = re.search(r'([0-9]*?)元/月', div_text).group()
            try:
                charge_mode = re.search(r'\((.*?)\)', div_text).group()[1:-1]
            except AttributeError:
                charge_mode = None
            information.extend([area, lease,direction, price, charge_mode])
            try:
                room = re.search(r'([0-9*?])室', ul_text).group()
            except AttributeError:
                room = None
            hall = re.search(r'([0-9*?])厅', ul_text).group()
            toilet = re.search(r'([0-9*?])卫', ul_text).group()
            information.extend([room, hall, toilet])
            # -----------------------------属于' <房源基本信息 >'------------------------------
            div = soup.find('div', class_='content__article__info')
            ul_list = div.find_all('ul')
            ul_text = ''
            for ul in ul_list:
                ul_text += ul.text
            check_in = re.search(r'入住：(.*?)\n', ul_text).group()[3:-1]
            term = re.search(r'租期：(.*?)\n', ul_text).group()[3:-1]
            tour = re.search(r'看房：(.*?)\n', ul_text).group()[3:-1]
            floor = re.search(r'楼层：(.*?)/', ul_text).group()[3:-1]
            total_floor = re.search(r'/(.*?)\n', ul_text).group()[1:-1]
            lift = re.search(r'电梯：(.*?)\n', ul_text).group()[3:-1]
            parking_spot = re.search(r'车位：(.*?)\n', ul_text).group()[3:-1]
            water = re.search(r'用水：(.*?)\n', ul_text).group()[3:-1]
            electrcity = re.search(r'用电：(.*?)\n', ul_text).group()[3:-1]
            gas = re.search(r'燃气：(.*?)\n', ul_text).group()[3:-1]
            heating = re.search(r'采暖：(.*?)\n', ul_text).group()[3:-1]
            information.extend([check_in, term, tour, floor, total_floor, lift, parking_spot, water, electrcity, gas, heating])
            print(information[0],'保存数据成功')
            filewriter.writerow(information)