import jieba
import csv
import random
from copy import deepcopy

# 导入一级二级三级词汇，可能挖空的词汇
with open("dictionary/LevelOne.csv", "r", encoding='utf8') as file:
    with open("dictionary/LevelTwo.csv", "r", encoding='utf8') as file1:
        with open("dictionary/LevelTwo.csv", "r", encoding='utf8') as file3:
            str1 = file.read()
            str2=file1.read()
            str3=file3.read()
            result1 = jieba.lcut(str1)
            result2 = jieba.lcut(str2)
            result3=jieba.lcut(str3)
            result1.extend(result2)
            result1.extend(result3)
            for i in result1:
                if i in [' ' , '\n' ,',' , '\ufeff' , '（' , '）' , "患者"]:
                    result1.remove(i)
            #print (result)
            strDict = {} #挖空的词
            for i in result1:
                strDict[i]=1
            file.close()
#对话的文本按行来挖空。
with open("./question/textQuestion3.txt", 'a', encoding='utf8') as file2:
    with open("原文.txt", "r", encoding='utf8') as f2:
    # 打开文件
        txt = f2.readlines()
      # key = []  # 存储挖空出来的词
        for data in txt:
            result = jieba.lcut(data)
            key=[]
            word = deepcopy(strDict)
            listOfStr = []  #储存原对话中的分词
            listLine = []  #需要挖空的词
            flag = True
            for i in result:
                for j in ",，'\n''!。？?《》；：“”‘’【】（）、[]{}:，-/":  #删除标点符号
                    if i==j:
                        flag = False
                        break
                if flag==True and i not in listOfStr:
                    listOfStr.append(i)
                flag = True
                #得到分词后地纯文本列表
            # print(data)
            # print(listOfStr)
            count = 0
            for i in listOfStr:
                for j in strDict:

                    if i == j:
                        listLine.append(i)  # 将在第一行出现的的挖空词汇单独拿到一个列表中.
            lenthOfListLine = len(listLine) #需挖空词的数量
            print(listLine)
            # for i in range(len(listLine)):
            #     if word[listLine[i]] == 0:
            #             lenthOfListLine = lenthOfListLine - 1
            LevelOne = 0
            LevelTwo = 0
            LevelThree=0
            for num in range(lenthOfListLine):
                if word[listLine[num]] == 0:
                    continue
                if lenthOfListLine > 10:
                    if LevelOne>=2 or LevelTwo>=4 or LevelThree>=5:
                        continue
                    Ran=random.randint(0,1)
                    if Ran==1:
                        data = data.replace(listLine[num],  '____',1)
                        # lenthOfListLine -= 1

                        key.append(listLine[num])
                        word[listLine[num]] = 0
                        if listLine[num] in result1:
                            LevelOne+=1
                        if listLine[num] in result2:
                            LevelTwo+=1
                        if listLine[num] in result3:
                            LevelThree+=1
                    else:
                        continue

                    if LevelOne>=2 and LevelTwo>=4 and LevelThree>=5:
                        break

                elif lenthOfListLine>0 and lenthOfListLine<=10:
                    data = data.replace(listLine[num], '____', 1)
                    # lenthOfListLine -= 1
                    key.append(listLine[num])
                    word[listLine[num]] = 0

                else:
                    break
            print(key)
            print(LevelOne)
            if key==[] or [] :
                continue
            else:
                with open ("./key/key3.csv",'a',encoding='utf8',newline='') as f1:
                    f_csv = csv.writer(f1)
                    f_csv.writerow(key)
                file2.write(data)
            # csv_writer.writerow(key)
f1.close()
f2.close()
file.close()
