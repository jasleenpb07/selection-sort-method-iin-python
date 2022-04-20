#this programm is created by jasleenpb07
#instagram @jasleenpb07

lst1=[34,5455,456,7,67,65]
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]>lst1[j]:
           temp=lst1[i]
           lst1[i]=lst1[j]
           lst1[j]=temp
print(lst1) 
        
