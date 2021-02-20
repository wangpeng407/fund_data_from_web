# fund_data_from_web

- 1 从[MedSCI梅斯](https://www.medsci.cn/sci/nsfc.do?page=1&sort_type=3)获取基金信息 ```fund_data1.py```
  - 但是该网站的一个弊端是最多显示34页，500条信息，导致抓取信息不全 
- 2 从[科学基金网](http://fund.sciencenet.cn)获取基金信息 ```fund_data2.py```
  - 需要注册账号，且该网站有隐藏信息,需要获取权限才能登陆
  - 频繁请求会有所限制
  - 抓取的内部链接一段时间后就会失效
  - 信息相对较全
  - 需要VIP收费💔

### 帮助信息
```
python fund_data1.py -h
```

```
python fund_data2.py -h
```

### 输出文件
- ```fund_data1.py```: out1.txt
- ```fund_data2.py```: out2.txt

### 使用示例见 ```run.sh```
```
Python 3.7.4 
使用前需安装好所需模块
```
