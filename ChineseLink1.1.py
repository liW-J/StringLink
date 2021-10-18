import jieba
import csv



#导入一级二级三级词汇，可能挖空的词汇
with open("LevelOne.csv","r",encoding='utf8') as file:
    str = file.read()
    result = jieba.lcut(str)

    for i in result:
        if i in [' ' , '\n' ,',' , '\ufeff' , '（' , '）' , "患者"]:
            result.remove(i)
    #print (result)
    strDict = {} #挖空的词
    for i in result:
        strDict[i]=1
    file.close()


#对话的文本按行来挖空。
with open("textQuesstion.txt", 'a', encoding='utf8') as file2:

    with open("原文.txt", "r", encoding='utf8') as f2:
    # 打开文件

        txt = f2.readlines()



        # key = []  # 存储挖空出来的词

        for data in txt:

            word = strDict
            result1 = jieba.lcut(data)
            key=[]



            #最多挖10个空
            #data = f.readline()  # 按行读取文件（符合对话的特点）
            #result1 = jieba.lcut(data) #将原对话进行分词


            listOfStr = []  #储存原对话中的分词
            listLine = []  #需要挖空的词

            flag = True
            for i in result1:
                for j in ",，'\n''!。？?《》；：“”‘’【】（）、[]{}:，/":  #删除标点符号
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
            lenthOfListLine = len(listLine)
            print(listLine)



            for i in range(lenthOfListLine):

                # print(lenthOfListLine)
                # print("第{}".format(i))

                if lenthOfListLine > 1:
                    # randomNum = random.randint(0, lenthOfListLine - 1)
                    # while strDict[listLine[randomNum]] == 0:
                    #     randomNum = random.randint(0, lenthOfListLine - 1)
                    #     count += 1
                    #
                    #     if count > lenthOfListLine:
                    #         break
                    #     # 如果已经挖空过 则再次随机挖空
                    # key.append(listLine[randomNum])
                    # strDict[listLine[randomNum]] = 0
                    for k in range(lenthOfListLine):
                        # if word[listLine[k]] != 0:
                            # randomNum = random.randint(0, lenthOfListLine - 1)
                        data = data.replace(listLine[k],  '__{}__'.format(i),1)
                        lenthOfListLine = lenthOfListLine - 1
                        key.append(listLine[k])


                        word[listLine[k]] = 0
                        count += 1

                        # else:
                        #     print(listLine[k])
                        #     continue





                    # 字符串不可变
                    #data = data.replace(listLine[randomNum], '____')
                    # count = count + 1
                    lenthOfListLine = lenthOfListLine - 1
                elif lenthOfListLine == 1:
                    k= 0
                    if word[listLine[k]] == 0:
                        lenthOfListLine = lenthOfListLine - 1

                        # randomNum = random.randint(0,lenthOfListLine-1)
                        # count+=1
                        # if count>lenthOfListLine:
                        #     break
                        continue
                    else:
                        data = data.replace(listLine[k], '__{}__'.format(i))
                        lenthOfListLine = lenthOfListLine - 1
                        key.append(listLine[k])



                        word[listLine[k]] = 0 #已经挖除的词 将其置零

                        data = data.replace(listLine[k],'__{}__'.format(data)) #如果只有一个相同的词，将它挖空
                        #file2.write(newData)
                        word[listLine[k]] = 0
                        # count = count + 1
                        lenthOfListLine = lenthOfListLine - 1


                elif lenthOfListLine == 0:
                    data= data
                    #file2.write(newData)
                    # count = count+1


                    break


                else:
                    break
            print(key)
            if key==[] or [] :
                continue

            else:
                with open ("key.csv",'a',encoding='utf8',newline='') as f1:
                    f_csv = csv.writer(f1)
                    f_csv.writerow(key)




                file2.write(data)



            # csv_writer.writerow(key)





f1.close()
f2.close()
file.close()
