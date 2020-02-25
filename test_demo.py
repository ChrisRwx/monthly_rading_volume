# -*- coding: utf-8 -*-
""""
# @File  : test.py
# @Author: Wenxin Ren
# @Date  : 2020/2/24 
"""""

import pandas as pd
import matplotlib.pyplot as plt
import os,time
from datetime import datetime


class DataShow():

    def __init__(self,datafile_name,trade_volume_datafile):
        self.father_dir = os.path.abspath(os.path.dirname(__file__))
        self.datafile = os.path.join(self.father_dir,datafile_name)
        self.heade_name = ['timestamp','price',"trade_volume"]
        self.trade_volume_datafile = trade_volume_datafile


    # 格式化时间
    @staticmethod
    def time_format(list1):
        list2 = []
        for i in list1:
            timeArray = time.localtime(i)
            time1 = time.strftime("%y/%m", timeArray)
            list2.append(time1)
        return list2

    #获取月交易量信息
    def monthly_trading_volume_info(self):
        # 读取文件
        data = pd.read_csv(self.datafile,names=self.heade_name)  # 读取csv文件内容
        data2 = pd.DataFrame(data)
        # 去掉重复项
        data2.drop_duplicates(keep='first',inplace=True)
        #去除价格为0的数据
        data3=data2[~data2['price'].isin([0])]
        # 时间戳转换为可读形式,只显示到月份
        time1 = DataShow.time_format(data3["timestamp"])
        # 将转换后的时间数据重新写入date3中
        data3['time_format'] = time1
        # 根据time_format的月份,算出每月总交易量
        trade_volume_sum = data3.groupby("time_format").agg({"trade_volume":sum})
        # 将按月份分组算出的交易量写入trade_volume_sum.csv
        trade_volume_sum.to_csv(os.path.join(self.father_dir, self.trade_volume_datafile))

    # 月交易量展示
    def monthly_trading_volume_display(self):
        datafile1 =os.path.join(self.father_dir, self.trade_volume_datafile)
        data4 = pd.read_csv(datafile1)  # 读取csv文件内容
        data5 = pd.DataFrame(data4)
        print(data5)
        # 绘制出折线图
        plt.plot(data5['time_format'], data5['trade_volume'])
        plt.title(u'Monthly trading volume display', fontsize=15)
        plt.xticks(rotation='vertical')
        plt.xlabel(u'months', fontsize=12)
        plt.ylabel(u'the volume of the trade ', fontsize=15)
        plt.show()

    def show(self):
        self.monthly_trading_volume_info()
        self.monthly_trading_volume_display()


if __name__ == '__main__':
    dateshow = DataShow(".btctradeCNY.csv",".trade_volume_sum.csv")
    dateshow.show()















# print("显示缺失值，缺失则显示为TRUE：\n", data.isnull())  # 是缺失值返回True，否则范围False
# print("---------------------------------\n显示每一列中有多少个缺失值：\n", data.isnull().sum())
