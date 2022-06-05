#-*- coding:utf-8 -*-
import jieba
from copy import deepcopy
from function import clear,department,clearPun,dig
import csv,time,random
from ltp import LTP
from function import disturb,dic
import random,re
#使用等级一、等级二的文件词汇 对原文的对话 进行挖空 生成textQuestion2.txt存放挖空后的对话＋key2.csv存放挖空后的答案]

def text_completion(data,c:int,n:int):

    strDict1,result1 = clear("./dictionary/LevelOne.csv")
    strDict2,result2 = clear("./dictionary/LevelTwo.csv")
    strDict3,result3 = clear("./dictionary/LevelThree.csv")
    strDict1.update(strDict2)
    strDict1.update(strDict3)

    with open("./dictionary/代词.csv", "r", encoding='utf8') as file:
        str1 = file.read()
        Result = str1.split("\n")
        for i in Result:
            if i in [' ', '\n', ',', '\ufeff', '（', '）', "患者"]:
                Result.remove(i)
    count = 0
    result = jieba.lcut(data)
    key=[]
    word = deepcopy(strDict1)
    listOfStr = []  #储存原对话中的分词
    listLine1 = []  #需要挖空的词
    listLine2 = []
    listLine3 = []
    clearPun(result, listOfStr)
        # 得到分词后的纯文本列表

    #判断科室类别
    with open("./中医疾病与病征编码.txt", 'r', encoding='utf8', newline='') as f:
        txt = []
        for line in f.readlines():
            curline = line.strip().split(" ")
            txt.append(curline[0])
    with open("dictionary/HSK.csv", 'r', encoding='utf8', newline='') as ff:
        words = []
        for line in ff.readlines():
            curline = line.strip().split(" ")
            words.append(curline[0])
    FLAG=True
    for i in result:
        for j in txt:
            if i==j or j in i:
                FLAG=False

    if FLAG==False:
        note = "该文本包含中医词汇，不能作为出题文本。"
        return note
    for i in listOfStr:
        for j in result1:
            if i == j:
                listLine1.append(i)  # 将在一行出现的的挖空词汇单独拿到一个列表中.
    for i in listOfStr:
        for j in result2:
            if i == j:
                listLine2.append(i)  # 将在一行出现的的挖空词汇单独拿到一个列表中.
    for i in listOfStr:
        for j in result3:
            if i == j:
                listLine3.append(i)  # 将在一行出现的的挖空词汇单独拿到一个列表中.
    lenthOfListLine = len(listLine1)+len(listLine2)+len(listLine3) #需挖空词的数量
    listLine = []
    listLine.extend(listLine1)
    listLine.extend(listLine2)
    listLine.extend(listLine3)
    if lenthOfListLine==0:
        note = "该文本找不到适合出题的词语！"
    # print(listLine1,listLine2,listLine3)
    LevelOne = 0
    LevelTwo = 0
    LevelThree = 0
    level = [listLine1,listLine2,listLine3]
    zi = ["一","二","三"]
    if level[c-1] == [] :
        note = "该文本不可出MCT{}级题！".format(zi[c-1])
        return note
    if lenthOfListLine < n:
        note = "该文本只能出{}道题！".format(n)
        return note

    if c == 1:
        num1 = n
        num2 , num3 = 0,0
    elif c == 2:
        num1 = int(0.3*n)
        num2 = n - num1
        num3 = 0
        if len(listLine2)<num2:
            num2 = len(listLine2)
            num1 = n - num2
    elif c == 3:
        num1 = int (0.3*n)
        num2 = int (0.3*n)
        num3 = n - num1 - num2
        if len(listLine3)<num3:
            num3 = len(listLine3)
            num2 = 0.7*(n - num3)
            if len(listLine2)<num2:
                num2 = len(listLine2)
            num1 = n - num2 - num3
    for num in range(lenthOfListLine):
        if word[listLine[num]] == 0:
            continue
        if lenthOfListLine :
            if LevelOne >= num1 and LevelTwo >= num2 and LevelThree >=num3:
                break
            else:
                LevelOne, count, data = dig(num, LevelOne, data, key, word, count, num1, result1, listLine)  # 一级词汇出2个
                LevelTwo, count, data = dig(num, LevelTwo, data, key, word, count, num2, result2, listLine)  # 二级词汇出4个
                LevelThree, count, data = dig(num, LevelTwo, data, key, word, count, num3, result3, listLine)  # 三级词汇出4个
        else:
            break
    AllKeys = []
    for j in key:
        keys = []
        keys.append(j)
        count = 0
        # 先匹配部位表和科室表
        for txt in ["./dictionary/部位.csv", "./dictionary/科室.csv", "./dictionary/疾病2字符.csv"]:
            newkeys, keys = dic(txt, count, keys)
            if len(keys) == 4:
                TYPE = "医学题"
                break

        if len(keys) != 4:
            with open("./dictionary/检查.csv", 'r', encoding='utf8', newline='') as f:
                with open("./dictionary/检查2字符.csv", "r", encoding='utf8', newline='') as newf:
                    word1 = []
                    for line in f.readlines():
                        curline = line.strip().split(" ")
                        word1.append(curline[0])
                        for i in ['﻿', '"']:
                            for num in word1:
                                if i in num:
                                    word1.remove(num)

                    word2 = []
                    for line in newf.readlines():
                        curline = line.strip().split(" ")
                        word2.append(curline[0])
                        for i in ['﻿', '"']:
                            for num in word2:
                                if i in num:
                                    word2.remove(num)

                    for word in word1:
                        if keys[0] in word:  # !!!!!应该是存在于还是完全等于
                            random.seed(time.time() + len(keys))
                            Ran = random.randint(0, len(word2) - 1)
                            newkeys = word2[Ran]
                            count += 1
                            keys.append(newkeys)
                            # 直到出满3题为止
                            while count != 3:
                                random.seed(time.time() + len(keys))
                                Ran = random.randint(0, len(word2) - 1)
                                newkeys = word2[Ran]
                                count += 1
                                keys.append(newkeys)
                        if len(keys) == 4:
                            TYPE = "医学题"
                            break
        ltp = LTP()
        seg, hidden = ltp.seg([j])
        pos = ltp.pos(hidden)
        # print(pos[0])
        if len(keys) != 4 and pos == [['r']]:
            newkeys, keys = dic("./dictionary/代词.csv", count, key)
            if len(keys) == 4:
                TYPE = "语法题"

        if len(keys) != 4:
            for txt in ["./dictionary/LevelThree.csv", "./dictionary/LevelTwo.csv", "./dictionary/LevelOne.csv"]:
                newkeys, keys = dic(txt, count, keys)
                if len(keys) == 4:
                    TYPE = "其它"
                    break
        keys.append(TYPE)
        AllKeys.append(keys)
        # print(keys)

    final = {"question":data,"options":AllKeys}

    return final

if __name__ == '__main__':
    data = input("输入文本：")
    c = input("输入等级：")
    n = input("输入出题个数：")
    c = eval(c)
    n = eval(n)
    print(text_completion(data,c,n))
