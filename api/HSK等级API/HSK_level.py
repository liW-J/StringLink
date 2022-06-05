# -*- coding: utf-8 -*-

import pandas as pd
from function import judge_HSK
import jieba

def HSK_Level(data):
    words = jieba.lcut(data)
    df1 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.1 一级词汇表",usecols=[0],header=None)
    df2 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.2 二级词汇表",usecols=[0],header=None)
    df3 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.3 三级词汇表",usecols=[0],header=None)
    df4 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.4 四级词汇表",usecols=[0],header=None)
    df5 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.5 五级词汇表",usecols=[0],header=None)
    df6 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.6 六级词汇表",usecols=[0],header=None)
    df7 = pd.read_excel("中文国际教育新标准-词汇.xlsx",sheet_name="6.7 七—九级词汇表",usecols=[0],header=None)
    time = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}

    for i in words:
        FLAG = False
        for j in range(1,8):
            name = "df" + str(j)
            if judge_HSK(eval(name),i,FLAG)== True:
                level = j
                time[level]+=1
                break
            else:
                level = None


    max_values = max(time.values())
    if max_values == 0:
        max_list = ["其它"]
    else:
        max_list = []
        for m, n in time.items():
            if n == max_values:
                max_list.append(m)
    # print(max_list)
    return max_list
if __name__ == '__main__':
    data = input("输入文本：")
    print(HSK_Level(data))
