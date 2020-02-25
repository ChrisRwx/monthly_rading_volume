 题目如下：
数据源为：
http://api.bitcoincharts.com/v1/csv/btctradeCNY.csv.gz
数据格式为：
column 1) the trade's timestamp, column 2) the price, column 3) the volume of the trade  

从数据集中找到合计交易量（volume）最大得那个月的数据。
要求：
1.timestamp要转换为可读形式
2.去掉重复以及价格为0得数据（如果存在）
3.画出交易量最大月份得价格曲线图(可以使用matplotlib）

最好是以Jupyter notebook的形式提交代码， 如果不熟悉也可将代码提交到github之后把链接给我。


注: 将.btctradeCNY.csv解压到test_demo同级目录运行,不然报错找不到文件!!!
    使用python版本为:3.6
