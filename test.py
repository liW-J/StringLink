#-*- coding:utf-8 -*-
# import csv
#
# headers = ['class','name','sex','height','year']
# #
# # rows = [
# #         [1,'xiaoming','male',168,23],
# #         [1,'xiaohong','female',162,22],
# #         [2,'xiaozhang','female',163,21],
# #         [2,'xiaoli','male',158,21]
# #     ]
#
# with open('test.csv','w',newline='')as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     # f_csv.writerows(rows)
# data="我不知道不知道不知道"
# data=data.replace("不知","嘿嘿",3)
# print(data)
# for i in range(5):
#     print(i)
#     data = data.replace("不知", '__{}__'.format(i))
#     print(data)

# with open("./中医疾病与病征编码.txt", 'r', encoding='utf8', newline='') as file:
#     for i in file:
#         i.strip('\n')
#         print(i)
#         break

# with open("./中医疾病与病征编码.txt", 'r', encoding='utf8', newline='') as f:
#     txt = []
#     for line in f.readlines():
#         curline=line.strip().split(" ")
#         txt.append(curline[0])ew
# print(txt)

# with open("LevelTwo.csv", 'r', encoding='utf8', newline='') as f:
#     word = []
#     for line in f.readlines():
#         curline = line.strip().split(" ")
#         word.append(curline[0])
# #     print(word)
# from function import disturb
# new=disturb("LevelTwo.csv", "碎石")
# print(new)
# new1=disturb("LevelTwo.csv", "碎石")
# print(new1)
# with open("./key/1.1key2.csv","r",encoding='utf8') as f4:
#     R=f4.readlines()
#     for i in range(len(R)):
#         print(R[i])
# from ltp import LTP
# encoding: UTF-8
import re
# txt="bcd"
# 将正则表达式编译成Pattern对象
# pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match('hello world!')

# if match:
    # 使用Match获得分组信息
    # print(match.group())
# print(re.sub("b+","#",txt))
# print(txt)
# print(result)
# ### 输出 ###
# # hello
#
# a=["1","2","3"]
# if "1" in a:
#     a.remove("2")
# print(a)
# ltp = LTP()
# for i in ["这么","我"]:
#     seg, hidden = ltp.seg([i])
#     pos = ltp.pos(hidden)
#     print(pos)
#     if pos[0][0]=='v':
#         print(True)
from function import dig
count=1
LevelOne=0
key=[]
result1=["我喝"]
listLine=["我喝"]
word={"我喝":0}
num=0
data="{'history': ['患者：前表性胃炎，__ 我喝纯牛奶好不好？养胃吗（男，22岁）', '医生：平时有什么不舒服吗？如果没有特别的，不用吃药，饮食上注意就可以。纯牛奶可以的。', '患者：平时吃一碗多饭胃又涨了，平时有点痛，我每天都会喝纯牛奶的。', '医生：去做胃镜了吗？', '患者：今年没有做，还是去年做的，', '医生：恩，应该没事，如果厉害的话，可以吃点奥美拉唑。', '医生：或者可以少食多餐，易消化的食物，多运动。', '患者：为什么老是打嗝。', '医生：有可能胀气。你喝了奶后，会厉害吗？', '患者：一样的。', '医生：那你先别喝牛奶了，牛奶容易胀气。', '医生：豆类食品最好先别吃。', '医生：平时可以多喝点小米稀饭，这个养胃，吃完饭不要立刻躺下。', '患者：豆类我先不吃，牛奶还要喝的，纯牛奶喝了没事，我只对酸奶有，喝酸奶会反酸。', '医生：嗯呢，那你试试。', '患者：每次都是一个小时后才躺下了，真是遭罪。', '医生：平时吃饭，也要注意，那些吃了不舒服，以后就少吃点。', '医生：慢性胃炎，都要靠慢慢的养。', '患者：好的太慢了，人都消瘦了，']}"
# data = data.replace(a, ' __' + str(count) + '__ ', 1)

# LevelOne,count,data=dig( 0, LevelOne, data, key, word,count,3, result1,listLine)


print(data)
a="__ "+'['+listLine[num]+']'
print(a)
if re.sub(a,"#",data)==data:
    print(True)
else:
    print(False)
data = data.replace(listLine[0], ' __' + str(count) + '__ ',1)