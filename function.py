# from docx.oxml.ns import qn
# from docx import Document
#-*- coding:utf-8 -*-
import time
import random,re
def clear(a):
    with open(a, "r", encoding='utf8') as file:
        str1 = file.read()
        # print(str1)

        #
        # result1 = jieba.lcut(str1)
        result1=str1.split("\n")
        # print(result1)

        for i in result1:
            if i in [' ', '\n', ',', '\ufeff', '（', '）', "患者"]:
                result1.remove(i)
        # print (result)
        strDict = {}  # 挖空的词
        for i in result1:
            strDict[i] = 1
        file.close()
        return strDict,result1
def clearCon(l=[]):
    flag = True
    for i in l:
        for j in ",，'\n''!。？?《》；：“”‘’【】（）、[]{}:，-/":  # 删除标点符号
            if i == j:
                flag = False
                break
        if flag == True and i not in l:
            l.append(i)
        flag = True

def clearPun(result,listOfStr):
    flag = True
    for i in result:
        for j in ",，'\n''!。？?《》；：“”‘’【】（）、[]{}:，-/":  # 删除标点符号
            if i == j:
                flag = False
                break
        if flag == True and i not in listOfStr:
            listOfStr.append(i)
        flag = True

def dig(num,Level,data,key, word,count,a,result=[],listLine=[]):
    # continuous=1
    Ran=random.randint(0,1)

    if Level < a:
        # print(a)
        # print(len(result))
        for i in range(len(result)):
            # print(listLine[num])
            # print(result[i])
            if listLine[num] == result[i]:
                if Ran == 1:
                    count+=1
                    S = "__ " + '[' + listLine[num] + ']'
                    if re.sub(S,"#",data)==data :
                        FLAG=True
                    else:
                        FLAG=False

                    if FLAG==False:
                        break
                    else:
                        data = data.replace(listLine[num], ' __' + str(count) + '__ ',1)
                        key.append(listLine[num])
                        # print(key)
                        word[listLine[num]] = 0
                        Level += 1

            else:
                continue
    return Level,count,data

def disturb(txt,key,T):#txt:要选词典；key:正确答案；T:随机数种子
    #如果词典中存在key，则在改词典中再次选择一个同义选项；否则返回False
    with open (txt,'r',encoding='utf8',newline='') as f:
        word = []
        for line in f.readlines():
            curline = line.strip().split(" ")
            word.append(curline[0])
            for i in ['﻿', '"']:
                for num in word:
                    if i in num:
                        word.remove(num)
        #word存储词库中出现的词
        # print(word)
        #如果这个词出现在词典中，就在词典中随机选另一个词
        for j in word:
            # print(j)
            # print(len(word))
            # newkey = word[Ran]
            if key in j:#存在于还是完全等于？
                random.seed(T)
                Ran = random.randint(0, len(word) - 1)
                newkey=word[Ran]
                #随机出来的选项不能与原词相等
                # while newkey==key:
                #     random.seed(T)
                #     Ran = random.randint(0, len(word) - 1)
                #     newkey = word[Ran]

                # print(newkey)
                return newkey
        return False


def option(NEWKEY=[]):
    RightKey = NEWKEY[0]
    random.seed(time.time()+random.randint(0,50))
    Ran = random.randint(0, 3)
    A = NEWKEY[Ran]
    NEWKEY.remove(A)
    print(NEWKEY)
    random.seed(time.time()+random.randint(0,50))
    Ran = random.randint(0, 2)
    B = NEWKEY[Ran]
    NEWKEY.remove(B)
    print(NEWKEY)
    random.seed(time.time()+random.randint(0,50))
    Ran = random.randint(0, 1)
    C = NEWKEY[Ran]
    NEWKEY.remove(C)
    print(NEWKEY)
    D = NEWKEY[0]
    return A,B,C,D,RightKey

def dic(txt,count,KEY=[]):
    newkey = disturb(txt, KEY[0], time.time() + len(KEY))
    if newkey != False:
        count += 1
        # print(newkey)
        KEY.append(newkey)
        # print(KEY)
        # 直到出满3题为止
        while count != 3:
            newkey = disturb(txt, KEY[0], time.time() + len(KEY))
            count += 1
            KEY.append(newkey)
    return newkey,KEY

def department(words=[]):#科室-疾病判断
    department = {}
    with open("./dictionary/test.info.json", 'r', encoding='utf8', newline='') as f:
        for line in f:
            line = eval(line)
            if line['department'] in department.keys():
                department[line['department']].append(line['disease'])
            else:
                department[line['department']] = []
                department[line['department']].append(line['disease'])
    # with open("./train.info.json", 'r', encoding='utf8', newline='') as f:
    #     for line in f:
    #         line = eval(line)
    #         if line['department'] in department.keys():
    #             department[line['department']].append(line['disease'])
    #         else:
    #             department[line['department']] = []
    #             department[line['department']].append(line['disease'])
    time = {}
    for key in department.keys():
        time[key] = 0
    for word in words:
        for key in department.keys():
            if word in department[key]:
                time[key] += 1
    max_values=max(time.values())
    if max_values==0:
        max_list=["其它"]
    else:
        max_list=[]
        for m,n in time.items():
            if n == max_values:
                max_list.append(m)
    # print(max_list)
    return max_list


def judge_HSK(level,word,FLAG):
    nrows = len(level)
    # print(nrows)
    for i in range(nrows):
        if i == 0:
            continue
        if word == level.iloc[i, 0]:
            # print(level.iloc[i, 0])
            FLAG = True
    return FLAG

def system(name,listOfStr):
    nrows = len(name)
    # print(listOfStr)
    # print(nrows)
    system = {"内分泌系统":[],"循环系统":[],"呼吸系统":[],"消化系统":[],"运动系统":[],"泌尿系统":[],"生殖系统":[]}
    time = {"内分泌系统":0,"循环系统":0,"呼吸系统":0,"消化系统":0,"运动系统":0,"泌尿系统":0,"生殖系统":0}
    for i in range(nrows):
        print()
        if i >6740 and i < 9668:
            kind = "内分泌系统"
            # print(kind)
            # print(name.iloc[i,0])
            system[kind].append(name.iloc[i,0])
            # print(system)
        elif i > 12336 and i < 14512:
            kind = "循环系统"
            system[kind].append(name.iloc[i,0])
        elif i > 14512 and i < 15459:
            kind = "呼吸系统"
            system[kind].append(name.iloc[i, 0])
        elif i > 15459 and i < 17775:
            kind = "消化系统"
            system[kind].append(name.iloc[i,0])
        elif i > 18885 and i < 21085:
            kind = "运动系统"
            system[kind].append(name.iloc[i,0])
        elif i > 21085 and i < 21697:
            kind = "泌尿系统"
            system[kind].append(name.iloc[i,0])
        elif i > 21697 and i < 21526:
            kind = "生殖系统"
            system[kind].append(name.iloc[i,0])
    systemList = []
    for i in listOfStr:
         for (k,v) in system.items():
             # print(v)
             if i in v:
                systemList.append(k)
         # print(systemList)
         for i in systemList:
             time[i]+=1
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





