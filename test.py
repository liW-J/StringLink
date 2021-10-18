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
data="我不知道不知道不知道"
# data=data.replace("不知","嘿嘿",3)
# print(data)
for i in range(5):
    print(i)
    data = data.replace("不知", '__{}__'.format(i))
    print(data)