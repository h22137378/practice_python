n1=input("請輸入第一個正整數：")
n2=input("請輸入第二個正整數：")

count1=-1 #n1各字串所在之10的次方數
count2=0 #n1各字串真實數字
count3=-1 #n2各字串所在之10的次方數
count4=0 #n2各字串真實數字
sum1=0 #n1數字相加之和
sum2=0 #n2數字相加之和
total=0 #兩數字相乘之結果

for i in range(-1, -len(n1)-1, -1): #從字串n1後面數到前面
    count1=count1+1
    for j in range(0, 10**count1, 1):
        count2=count2+int(n1[i])
    sum1=sum1+int(count2)
    count2=0
for p in range(-1, -len(n2)-1, -1): #從字串n2後面數到前面
    count3=count3+1
    for h in range(0, 10**count3, 1):
        count4=count4+int(n2[p])
    sum2=sum2+count4
    count4=0
for k in range(0,sum2): #兩數相乘
    total=total+sum1
print(total)








