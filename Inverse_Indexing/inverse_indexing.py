import json
with open(r"C:\Users\Dell\Desktop\Mini Project\Appy\database_Aparajita_Indexed.json") as idx:
    data1=json.load(idx)
dicts={}
page_no=0
page=0
import csv
with open(r"C:\Users\Dell\Desktop\Mini Project\database_Souradip.csv",encoding='utf-8') as csvfile:
    data2=csv.reader(csvfile)
    for i in data2: 
        if page==0:
            page=page+1
            continue
        x=i[2]
        date=int(x[-4:]) #year
        m=x[:3]
        if m=="Jan":
            month=1
        elif m=="Feb":
            month=2
        elif m=="Mar":
            month=3
        elif m=="Apr":
            month=4
        elif m=="May":
            month=5
        elif m=="Jun":
            month=6
        elif m=="Jul":
            month=7
        elif m=="Aug":
            month=8
        elif m=="Sep":
            month=9
        elif m=="Oct":
            month=10
        elif m=="Nov":
            month=11
        else:
            month=12
        date=date*100+month #month
        day=0
        flag=0
        for da in x:
            if da.isdigit():
                flag=1
                day=day*10+int(da)
            if da==" " and flag==1:
                break
        date=date*100+day #day
        url=i[5] #url
        for keyword in data1[page_no]: 
            if keyword in dicts:
                dicts[keyword].append([(int(data1[page_no][keyword]*1000)),date,url,i[6],i[0]])
            else:
                dicts[keyword]=[]
                dicts[keyword].append([(int(data1[page_no][keyword]*1000)),date,url,i[6],i[0]]) 
        date=0
        page_no=page_no+1
        page=page+1
    for p1 in dicts:
        dicts[p1].sort(key=lambda x1: (x1[0],x1[1]), reverse=True)
    
#with open(r"C:\Users\Dell\Desktop\Mini Project\Appy\database_Aparajita_Inverse_Indexed.json", "w") as fp:
   #json.dump(dicts, fp)


#import csv
#with open(r"C:\Users\Dell\Desktop\Mini Project\database_Appycsv.csv", 'w') as f:
    #for key in dicts.keys():
        #f.write("%s,%s\n"%(key,dicts[key]))
#k=2
#for i in dicts:
#    for j in dicts[i]:
#        if(k==2):
            #print(j)
#            print(j[0],j[1],sep="\n")
#    k=k+1

#dicts=
#{
#    "ai": [[156,20201209,"link"],[196,20200409,"link"]],
#    "corona":[[156,20201209,"link"],[196,20200409,"link"]]
#}