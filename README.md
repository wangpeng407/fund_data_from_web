# fund_data_from_web

```
python fund_data.py -h
usage: fund_data.py [-h] -k KEY_WORDS [-o OUTFILE]

Version 1.0 根据关键词从 https://www.medsci.cn/sci/nsfc.do?page=1&sort_type=3 抓取基金
使用示例: python fund_data.py -k 代谢组 -o metabolite.fund.txt

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_WORDS, --key_words KEY_WORDS
                        Input ket words
  -o OUTFILE, --outfile OUTFILE
                        output file
wangpeng@wangpengs-MacBook-Pro 14:19:25 ~
```

### 输出文件
- metabolite.fund.txt
```
课题	负责人	单位	金额	类型	学科代码	开始时间
基于血外泌体代谢组学和肺CT影像组学预测新冠状病毒肺炎患者预后和抗病毒疗效及其机制研究	金阳	华中科技大学	120.0万元	医学科学	H1911医学科学部	202003
组学大数据解析植物演化过程中代谢组进化规律和种群特异代谢调控	吴雪婷	中国科学院上海生命科学研究院	25.0万元	青年科学基金项目	C060701生命科学	202001
```
