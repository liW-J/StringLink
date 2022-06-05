import csv
with open("./dictionary/MCT.csv", 'r', encoding='utf8', newline='') as f:
    with open("./dictionary/HSK6-9.csv", 'r', encoding='utf8', newline='') as ff:
        with open("./dictionary/HSK.csv", 'a', encoding='utf8', newline='') as fff:
            fff_csv = csv.writer(fff)

            list1=[]
            list2=[]
            for i in ff:
                list1.append(i)
            for j in f:
                list2.append(j)
            print(list1)
            print(list2)

            for i in list1:
                flag = True
                for j in list2:
                    if i[0] in j:
                        print(11)
                        flag=False
                if flag!= False:
                    fff_csv.writerow(i[0])







