# -*- coding: utf-8 -*-

import pandas as pd
from function import judge_HSK
import jieba

def HSK_Level(data):
    words = jieba.lcut(data)
    print(words)
    time = {1: 0, 2: 0, 3: 0}
    df1 = pd.read_excel("LevelOne.xlsx",usecols=[0],header=None)
    df2 = pd.read_excel("LevelTwo.xlsx",usecols=[0],header=None)
    df3 = pd.read_excel("LevelThree.xlsx",usecols=[0],header=None)

    for i in words:
        FLAG = False
        for j in range(1,4):
            name = "df" + str(j)
            if judge_HSK(eval(name),i,FLAG)== True:
                level = j
                time[level] += 1
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
