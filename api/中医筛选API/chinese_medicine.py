#-*- coding:utf-8 -*-
import jieba
import csv
import random
from copy import deepcopy
from function import clear,department,clearPun,dig

import random,re
#使用等级一、等级二的文件词汇 对原文的对话 进行挖空 生成textQuestion2.txt存放挖空后的对话＋key2.csv存放挖空后的答案]
def chinese_medicine(data):
    result = jieba.lcut(data)
    key=[]
    listOfStr = []  #储存原对话中的分词
    clearPun(result, listOfStr)
    with open("./中医疾病与病征编码.txt", 'r', encoding='utf8', newline='') as f:
        txt = []
        for line in f.readlines():
            curline = line.strip().split(" ")
            txt.append(curline[0])
    FLAG=True
    for i in result:
        for j in txt:
            if i == j or j in i:
                FLAG = False
    return FLAG



if __name__ == '__main__':
    data = input("输入文本：")
    print(chinese_medicine(data))