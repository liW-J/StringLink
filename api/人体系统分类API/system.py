#-*- coding:utf-8 -*-
import jieba
import csv
import random
from copy import deepcopy
from function import clear,system,clearPun,dig
import pandas as pd

import random,re
#使用等级一、等级二的文件词汇 对原文的对话 进行挖空 生成textQuestion2.txt存放挖空后的对话＋key2.csv存放挖空后的答案]

def judge_system(data):
    # print(data)
    result = jieba.lcut(data)
    listOfStr = []  #储存原对话中的分词
    # print(result)
    clearPun(result, listOfStr)
    df1 = pd.read_excel("国家临床版2.0疾病诊断编码（ICD-10）.xlsx", sheet_name="国家临床版2.0诊断编码（ICD-10）", usecols=[1], header=None)
    sys = system(df1,listOfStr)
    return sys
if __name__ == '__main__':
    data = input("输入文本：")
    # data = data.decode('utf-8')
    print(judge_system(data))