import random,time,json ,pprint

room1=['ranjan','shubhash','Shubhdeep','Pawan','SurajShah','Raju BHai',"Rajkumar","Dhruv"]
room6=[]
room7=['Riyaaz',"Shabid",'Prathmesh',"Ankit","Harshal",'Pravin',]
room8=['Tushar',"Sampath",'Suraj kumar','Hemant','Siddik','Anmol']
room11=['Priyanshu','Nasir','Navid','Vishal M']
room10=['Amarpal','Aarif','Satpal','Abhay','SaiKiran']
room12=['Rahul Sr',"Dipesh",'Akshit bhatt','Amol m',"Anurag",'Akshay pande','Umesh','Parmeshwar']

total=[room1+room10+room6+room12+room7+room8+room11]
random.shuffle(total)
c=[]
x=[i for i in range(1,54)]
random.shuffle(x)
for i in total:
    random.shuffle(i)
    for j,k in zip(x,i):
        d={j:k}
        # print(d)
        c.append(d)
      

# print(c)
lst=[]




for i in c:
    for j in i:
        if j%2==0:
            d={'name':i[j],'bed':j,'Position':'lower-side'}
            lst.append(d)
            # pprint.pprint(d)
            # time.sleep(5)
        else:
            d={'name':i[j],'bed':j,'Position':'upper-side'}
            lst.append(d)
            # pprint.pprint(d)

            # time.sleep(5)

pprint.pprint(lst)  

# r1=[1-10]
# r6=[11-20]
# r7=[21-28]
# r8=[29-34]
# r10=[35-42]
# r12=[43-52]

f=open('room_shuffle.json','w')
json.dump(lst,f,indent=5)
f.close()


