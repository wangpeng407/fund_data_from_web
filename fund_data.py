#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import argparse
import urllib
from urllib import request
from bs4 import BeautifulSoup

def parse_args():
    parser = argparse.ArgumentParser(description=
                                    "Version 1.0 根据关键词从 "
                                    "https://www.medsci.cn/sci/nsfc.do?page=1&sort_type=3"
                                    " 抓取基金\n"
                                    "使用示例: python " + sys.argv[0] + " -k 代谢组 -o metabolite.fund.txt\n",
                                    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-k", "--key_words", type=str, required=True,
                        help="Input ket words\n")
    parser.add_argument("-o", "--outfile", type=str, required=False, default='out.xls',
                        help="output file\n")
    args = parser.parse_args()
    return args


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Host": "www.medsci.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def extract_cont(conts):
    cont_dict = dict([(i.split("：")[0], i.split("：")[1]) for i in conts])
    return cont_dict

def get_page_num(url):
    first_r = requests.get(url=url, headers=headers)
    first_r2 = BeautifulSoup(first_r.content, "html.parser", from_encoding="utf-8")
    page_num = int(first_r2.find('span', class_="page-info-right").get_text().split('/')[-1].replace('页', ''))
    return page_num

def main():
    args = parse_args()
    chn_key_str = args.key_words
    outfile = args.outfile
    filewrite = open(outfile, 'w')
    trans_str = urllib.request.quote(chn_key_str)
    prefix_url = "https://www.medsci.cn/sci/nsfc.do?page="
    suffix_url = "&sort_type=3"
    temp_url = prefix_url + "1" + "&txtitle=" + trans_str + suffix_url
    page_num = get_page_num(url=temp_url)
    filewrite.write('课题\t负责人\t单位\t金额\t类型\t学科代码\t开始时间\t具体链接\n')
    for p in range(0, page_num):
        temp_url = prefix_url + str(p + 1) + "&txtitle=" + trans_str + suffix_url
        r = requests.get(url=temp_url, headers=headers)
        r2 = BeautifulSoup(r.content, "html.parser", from_encoding="utf-8")
        all_cont = (r2.find_all('div', class_='item-font'))
        for i in range(0, len(all_cont)):
            temp_conts = [i.get_text() for i in all_cont[i].find_all('p')]
            temp_dict_conts = extract_cont(temp_conts)
            temp_dict_conts['标题'] = (all_cont[i].find('a', class_=['ms-link']).get_text())
            temp_dict_conts['具体链接'] = all_cont[i].find('a', class_ = ['ms-link']).get('href')
            line_cont = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                temp_dict_conts['标题'],
                temp_dict_conts['负责人'],
                temp_dict_conts['单位'],
                temp_dict_conts['金额'],
                temp_dict_conts['类型'],
                temp_dict_conts['学科代码'],
                temp_dict_conts['开始时间'],
                temp_dict_conts['具体链接'])
            filewrite.write(line_cont + "\n")
    filewrite.close()

if __name__ == '__main__':
    main()
