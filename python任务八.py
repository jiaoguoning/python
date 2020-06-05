# -*- coding: utf-8 -*-
"""
Created on Fri May  8 07:20:27 2020

@author: HP
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re 

def get_url(urls):
    '''获得网页全部代码'''
    html = urlopen(urls)
    htmlcode = BeautifulSoup(html, 'html.parser')
    htmlcode_str = str(htmlcode)

    # 去除换行符和制表符方便匹配
    htmlcode_str = re.sub('\n', ' ', htmlcode_str)
    htmlcode_str = re.sub('\t', ' ', htmlcode_str)
    
    return htmlcode_str

def get_content(htmlcode_str):
    '''从字符中获取有用信息'''
    return re.findall(r'<ul class="menu">(.*?)</ul>', htmlcode_str)

def get_time_title(content):
    '''提取时间和标题'''
    content = str(content)
    time = list()
    title = list()
    lis = re.findall(r'<li>(.*?)</li>', content)
    for i in lis:
        times = re.findall(r'<time datetime.*><span.*>(.*?)</span>(.*?)</time>', i)
        titles = re.findall(r'<a href.*>(.*?)</a>', i)
        time.append(times[0][0]+times[0][1])
        title.extend(titles)
    return time, title

def save_as_csv(matrix):
    '''将新闻信息存入csv文件'''
    with open('python-latest-news.csv', 'wt') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(matrix)
        
def main():
    '''
    获得网页所有代码，提取所需的信息
    '''
    content = get_content(get_url('https://www.python.org'))
    time, title = get_time_title(content[0])
    news = list()
    for i in range(len(time)):
        news.append([time[i],title[i]])
    save_as_csv(news)
main()






