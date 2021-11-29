#-*- coding:utf-8 -*-
import jieba
import csv
import random
from copy import deepcopy
from function import clear,clearCon,clearPun,dig
from docx.oxml.ns import qn
from docx import Document
# from function import writeKey
from ltp import LTP
import random,re
#使用等级一、等级二的文件词汇 对原文的对话 进行挖空 生成textQuestion2.txt存放挖空后的对话＋key2.csv存放挖空后的答案]

strDict1,result1=clear("./dictionary/LevelOne.csv")
strDict2,result2=clear("./dictionary/LevelTwo.csv")
strDict3,result3=clear("./dictionary/代词.csv")
strDict1.update(strDict2)
strDict1.update(strDict3)

with open("./dictionary/代词.csv", "r", encoding='utf8') as file:
    str1 = file.read()

    Result = str1.split("\n")

    for i in Result:
        if i in [' ', '\n', ',', '\ufeff', '（', '）', "患者"]:
            Result.remove(i)
#对话的文本按行来挖空。
with open("question/textQuestion2.3.txt", 'a', encoding='utf8') as file2:
    with open("demo.txt", "r", encoding='utf8') as f2:
    # 打开文件
        txt = f2.readlines()
      # key = []  # 存储挖空出来的词
        for data in txt:

            count = 0
            result = jieba.lcut(data)
            key=[]
            word = deepcopy(strDict1)
            listOfStr = []  #储存原对话中的分词
            listLine = []  #需要挖空的词
            clearPun(result, listOfStr)
                # 得到分词后的纯文本列表
            # print(data)
            # print(listOfStr)
            with open("./中医疾病与病征编码.txt", 'r', encoding='utf8', newline='') as f:
                txt = []
                for line in f.readlines():
                    curline = line.strip().split(" ")
                    txt.append(curline[0])
            FLAG=True
            for i in result:
                for j in txt:
                    if i==j:
                        FLAG=False
            if FLAG==False:
                continue
            ltp = LTP()
            for i in listOfStr:
                seg, hidden = ltp.seg([i])
                pos = ltp.pos(hidden)
                print(pos[0])
                if pos[0] == ['r'] and (pos[0][0] in Result):
                    listLine.append(i)
                    print(i)
                    continue
                for j in strDict1:
                    if i == j:
                        listLine.append(i)  # 将在一行出现的的挖空词汇单独拿到一个列表中.


            lenthOfListLine = len(listLine) #需挖空词的数量
            print(listLine)

            LevelOne = 0
            LevelTwo = 0
            Else=0
            for num in range(lenthOfListLine):
                if word[listLine[num]] == 0:
                    continue
                if lenthOfListLine > 10:
                    Ran=random.randint(0,1)
                    if LevelOne>=3 and LevelTwo>=5:
                        break
                    else:
                        LevelOne,count,data=dig( num, LevelOne, data, key, word,count,3, result1,listLine)#一级词汇出4个
                        LevelTwo,count,data=dig( num, LevelTwo, data, key, word,count,5, result2,listLine)#二级词汇出6个
                        Else,count,data=dig( num, Else, data, key, word,count,2,result3, listLine)#语法词出2个
                elif lenthOfListLine>0 and lenthOfListLine<=10: #如果挖空词语不超过10个，全部挖掉
                    S = "__ " + '[' + listLine[num] + ']'
                    if re.sub(S, "#", data) == data:
                        flag = True
                    else:
                        flag = False

                    if flag == False:
                        break
                    else:
                        count += 1
                        data = data.replace(listLine[num], ' __'+str(count)+'__ ', 1)
                        # lenthOfListLine -= 1
                        key.append(listLine[num])
                        for i in range(len(result1)):
                            if listLine[num] == result1[i]:
                                    LevelOne += 1
                        for i in range(len(result2)):
                            if listLine[num] == result2[i]:
                                    LevelTwo += 1
                        for i in range(len(result3)):
                            if listLine[num] == result3[i]:
                                    Else += 1
                        word[listLine[num]] = 0
                else:
                    break
            # print(count)
            # print(LevelTwo)
            # print(LevelOne)
            print(key)
            print(data)
            if key==[] or [] :
                continue
            else:
                with open ("key/key2.3.csv", 'a', encoding='utf8', newline='') as f1:
                    f_csv = csv.writer(f1)
                    f_csv.writerow(key)
                file2.write(data)
            # csv_writer.writerow(key)
f1.close()
f2.close()

