# fund_data_from_web

- 1 从[MedSCI梅斯](https://www.medsci.cn/sci/nsfc.do?page=1&sort_type=3)获取基金信息，但是该网站的一个弊端是最多显示34页，500条信息，导致抓取信息不全 ```fund_data1.py```
- 2 从[科学基金网](http://fund.sciencenet.cn)获取基金信息，但是需要注册账号，该网站有隐藏信息，频繁请求会有所限制，而且一段时间后链接会失效；但是信息较全 ```fund_data2.py```

### 帮助信息
```
python fund_data1.py -h
usage: fund_data1.py [-h] -k KEY_WORDS [-o OUTFILE]

Version 1.0 根据关键词从 https://www.medsci.cn/sci/nsfc.do?page=1&sort_type=3 抓取基金
使用示例: python fund_data1.py -k 代谢组 -o metabolite.fund.txt

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_WORDS, --key_words KEY_WORDS
                        Input ket words
  -o OUTFILE, --outfile OUTFILE
                        output file
```

```
python fund_data2.py -h
usage: fund_data2.py [-h] -k KEY_WORDS -u USERNAME [-p PASSWORD] [-s START]
                     [-e END]

Rerieve fund data from http://fund.sciencenet.cn

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_WORDS, --key_words KEY_WORDS
                        Input keywords.
  -u USERNAME, --username USERNAME
                        input your username.
  -p PASSWORD, --password PASSWORD
                        input the password.
  -s START, --start START
                        start year
  -e END, --end END     end year
```

### 输出文件
- ```fund_data1.py```: out1.txt
- ```fund_data2.py```: out2.txt
