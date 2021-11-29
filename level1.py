import jieba
import csv
import random
from copy import deepcopy
from function import clear

# 导入一级二级三级词汇，可能挖空的词汇
# with open("LevelOne.csv", "r", encoding='utf8') as file:
#     str = file.read()
#     result = jieba.lcut(str)
#
#     for i in result:
#         if i in [' ', '\n', ',', '\ufeff', '（', '）', "患者"]:
#             result.remove(i)
#     #print (result)
#     strDict = {}  # 挖空的词
#     for i in result:
#         strDict[i] = 1
#     file.close()
strDict,result1=clear("LevelOne.csv")

with open("./quesstion/textQuesstion1.txt", 'a', encoding='utf8') as file2:
    with open("原文.txt", "r", encoding='utf8') as f2:
        # 打开文件

        txt = f2.readlines()
      # key = []  # 存储挖空出来的词
        for data in txt:
            result1 = jieba.lcut(data)
            key = []
            word = deepcopy(strDict)
            listOfStr = []  # 储存原对话中的分词
            listLine = []  # 需要挖空的词
            flag = True
            for i in result1:
                for j in ",，'\n''!。？?《》；：“”‘’【】（）、[]{}:，-/":  # 删除标点符号
                    if i == j:
                        flag = False
                        break
                if flag and i not in listOfStr:
                    listOfStr.append(i)
                flag = True
                # 得到分词后地纯文本列表
            # print(data)
            # print(listOfStr)
            count = 0
            for i in listOfStr:
                for j in strDict:
                    if i == j:
                        listLine.append(i)  # 将在第一行出现的的挖空词汇单独拿到一个列表中.
            lenthOfListLine = len(listLine)  # 需挖空词的数量
            print(listLine)
            LevelOne = 0
            LevelTwo = 0
            for num in range(lenthOfListLine):
                if word[listLine[num]] == 0:
                    continue
                # print(lenthOfListLine)
                # print("第{}".format(i))
                if lenthOfListLine > 10:
                    Ran = random.randint(0, 1)
                    if LevelOne >= 10:
                        break

                    if Ran == 1:
                        data = data.replace(listLine[num], '____', 1)
                        key.append(listLine[num])
                        word[listLine[num]] = 0
                        if listLine[num] in result1:
                            LevelOne += 1
                    else:
                        continue
                elif lenthOfListLine > 0 and lenthOfListLine <= 10:
                    data = data.replace(listLine[num], '____', 1)
                    key.append(listLine[num])
                    word[listLine[num]] = 0
                else:
                    break
            print(key)
            if key == [] or []:
                continue

            else:
                with open("./key/key1.csv", 'a', encoding='utf8', newline='') as f1:
                    f_csv = csv.writer(f1)
                    f_csv.writerow(key)
                file2.write(data)
            # csv_writer.writerow(key)


f1.close()
f2.close()
file2.close()
