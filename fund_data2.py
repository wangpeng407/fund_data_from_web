#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
import requests
import argparse
from urllib import request
from bs4 import BeautifulSoup
import logging
from lxml import html
from time import sleep
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s: %(levelname)s: %(message)s')
logging.basicConfig(level=logging.WARNING, format='%(asctime)s: %(levelname)s: %(message)s')

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

session = requests.session()

def parse_args():
    parser = argparse.ArgumentParser(description=
                                    "Rerieve fund data from http://fund.sciencenet.cn",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-k", "--key_words", type=str, required=True,
                        help="Input keywords.\n")

    parser.add_argument('-u', '--username', type=str, required=True,
                        help="input your username.\n")

    parser.add_argument('-p', '--password', type=str,required=False,
                        help='input the password.\n')

    parser.add_argument('-s', '--start', type=int, required=False, default=2020,
                        help='start year')

    parser.add_argument('-e', '--end', type=int, required=False, default=2020,
                        help='end year')

    args = parser.parse_args()
    return args

def get_login_info(login_url, username, password):
    result = session.get(login_url)

    tree = html.fromstring(result.text)

    #extract hidden id value
    token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]

    payload = { 'phone' : username, 'password' : password, '_token' : token }

    return payload

def get_next_link_and_scrape_contents(url, mainurl, login_url,
                                      payload, sign=1, run_loop=True, login=True):
    # check if login is successful
    if login:
        try:
            result = session.post(login_url, data=payload, headers=headers)
            if result.status_code == 200:
                logging.info('login successfully!\n')
        except:
            logging.warning('Failed login, please check username and password\n!')
    # check if retrieve url is ok
    try:
        temp_res = session.get(url, headers=headers)
        temp_soup = BeautifulSoup(temp_res.content, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error('Failed request {}: {}, try again later.'.format(url, e))

    temp_batch_links = temp_soup.find_all("div", class_='resultLst')[0].find_all('a')
    # scrape internal links one by one
    if run_loop:
        for i in temp_batch_links:
            url_i = i.get('href')
            random_sleep_time = random.uniform(3, 8)
            try:
                sub_temp_res = session.get(url_i, headers=headers)
                sub_temp_soup = BeautifulSoup(sub_temp_res.content, "html.parser")
            except requests.exceptions.RequestException as e:
                logging.error('Failed request {}: {}, try again later.'.format(url_i, e))
                sleep(random_sleep_time)
                continue
            sub_temp_cont = sub_temp_soup.find_all("div", class_="v_con")
            sub_temp_res = [i.get_text() for i in sub_temp_cont[0].find_all('td')]
            sub_temp_title = sub_temp_cont[0].find('h1').get_text()
            print(sub_temp_title +"\t" + "\t".join(sub_temp_res))
            sleep(random_sleep_time)
    temp_all_big_links = temp_soup.find_all("span", class_="btn")
    # scrape main links next by next
    try:
        next_link = [i.find('a').get('href') for i in temp_all_big_links if i.find('a')][-1]
    except:
        # if no next links, stop
        return None
    sign = sign + 1
    sleep(random.uniform(3, 8))
    match_str = 'page=' + str(sign) + '&'
    if match_str in next_link:
        logging.info('#{}: {}\n'.format(sign, next_link))
        try:
            get_next_link_and_scrape_contents(next_link, mainurl, login_url,
                                              payload=payload, sign=sign,
                                              run_loop=True, login=False)
        except:
            random_sleep_except = random.uniform(300, 360)
            sleep(random_sleep_except)
            get_next_link_and_scrape_contents(next_link, mainurl, login_url,
                                              payload=payload, sign=sign,
                                              run_loop=False, login=True)
    else:
        return None

def print_tab_header():
    print("课题名称\t批准号\t学科分类\t项目负责人\t职称\t单位\t金额\t项目类别\t研究期限\t中文主题词\t英文主题词\t中文摘要\t英文摘要")

def main():
    args = parse_args()
    kw = request.quote(args.key_words)

    login_url = 'http://fund.sciencenet.cn/login'

    format_url = 'http://fund.sciencenet.cn/search?name=' + kw + \
                 '&code=&yearStart=' \
                 + str(args.start) + '&yearEnd=' + str(args.end) \
                 + '&subject=&category=&fundStart=&fundEnd=&submit=list'
    payload = get_login_info(login_url, username=args.username, password=args.password)
    print_tab_header()
    get_next_link_and_scrape_contents(url=format_url, mainurl=format_url,
                                      login_url=login_url, payload=payload,
                                      sign=1, run_loop=True, login=True)

if __name__ == '__main__':
    main()
