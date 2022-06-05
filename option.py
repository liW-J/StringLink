import csv,time,random
from ltp import LTP
from function import disturb,dic
with open("key/key1.csv", 'r', encoding='utf8', newline='') as f1:
    with open("newKey/newKey1.csv", 'a', encoding='utf8', newline='') as f2:
        key=f1.readlines()
        word=[]#key中的答案是按照每组对话的形式存入的 newkey中的答案是按照每题的形式存入的
        for line in key:
            line=line.strip('\r\n')
            key=line.split(",")
            # print(key)
            for i in key:
                word.append(i)
        # print(word)
        f_csv = csv.writer(f2)
        for j in word:
            print(j)
            key=[]
            key.append(j)
            count=0
            #先匹配部位表和科室表
            for txt in ["./dictionary/部位.csv","./dictionary/科室.csv","./dictionary/疾病2字符.csv"]:
                newkey,key = dic(txt, count,key)
                if len(key)==4:
                    TYPE="医学题"
                    break
            
            if len(key)!=4:
                with open("./dictionary/检查.csv", 'r', encoding='utf8', newline='') as f:
                    with open("./dictionary/检查2字符.csv","r",encoding='utf8',newline='') as newf:
                        word1 = []
                        for line in f.readlines():
                            curline = line.strip().split(" ")
                            word1.append(curline[0])
                            for i in ['﻿', '"']:
                                for num in word1:
                                    if i in num:
                                        word1.remove(num)

                        word2=[]
                        for line in newf.readlines():
                            curline = line.strip().split(" ")
                            word2.append(curline[0])
                            for i in ['﻿', '"']:
                                for num in word2:
                                    if i in num:
                                        word2.remove(num)
            
                        for word in word1:
                            if key[0] in word:  # !!!!!应该是存在于还是完全等于
                                print(11)
                                random.seed(time.time()+len(key))
                                Ran = random.randint(0, len(word2)-1)
                                newkey = word2[Ran]
                                count += 1
                                print(newkey)
                                key.append(newkey)
                                # 直到出满3题为止
                                while count != 3:
                                    random.seed(time.time() + len(key))
                                    Ran = random.randint(0, len(word2) - 1)
                                    newkey = word2[Ran]
                                    count += 1
                                    key.append(newkey)
                            if len(key)==4:
                                TYPE="医学题"
                                break
            ltp = LTP()
            seg, hidden = ltp.seg([j])
            pos = ltp.pos(hidden)
            # print(pos[0])
            if len(key)!=4 and pos == [['r']]:
                newkey,key= dic("./dictionary/代词.csv", count,key)
                if len(key) == 4:
                    TYPE = "语法题"

            if len(key)!=4:
                for txt in ["./dictionary/LevelThree.csv","./dictionary/LevelTwo.csv","./dictionary/LevelOne.csv"]:
                    newkey,key = dic(txt, count,key)
                    if len(key)==4:
                        TYPE = "其它"
                        break
            key.append(TYPE)
            print(key)

            f_csv.writerow(key)

# # file2.write(data)