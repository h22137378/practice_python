'''5-1
n=input("請輸入一整數字串(半形逗號分隔):")
n=n.split(',')
n=list(n) #轉換成串列
print(n)

s=set()

i=int(0)
s.update(n[i])
print(s)

while(s!=()):
    i=int(n[i])
    s.update(n[i])
    if(i==0):
        break
print(s)
print("長度："+str(len(s)))
'''

'''5-2
n1=int(input("請輸入第一個數字a:"))
n2=int(input("請輸入第二個數字b:"))

def compute(a,b):
    sum=0
    for i in range(a,b+1,1):
        sum+=i
    print("a加到b為:"+str(sum))
        
compute(n1,n2)
'''

'''5-3
list_n=[]
n=int(input("請輸入一整數："))
while(n!=-9999):
    list_n.append(n)
    n=int(input("請輸入一整數："))
if(n==-9999):
    t=tuple(list_n)   #把串列轉成數組
    print(t)          #顯示數組
    print("length:"+str(len(list_n))) #顯示長度
    max=list_n[0]
    min=list_n[0]
    for i in range(0,len(list_n),1):
        if(list_n[i]>max):
            max=list_n[i]
        if(list_n[i]<min):
            min=list_n[i]
    print("max:"+str(max)+"\n"+"min:"+str(min)) #顯示最大最小值
'''

'''5-4
sum=0
for i in range(1,10,1):
    for j in range(1,10,1):
        sum=i*j
        print(str(i)+"*"+str(j)+"="+str(sum), end='\t')
    print('\n')
'''

'''5-5
n1=input("請輸入第一個分數(ex:1,2)：")
n2=input("請輸入第二個分數(ex:1,2)：")
n1=n1.split(',')
n2=n2.split(',')
n1=list(n1)
n2=list(n2)
x=int(n1[0])
y=int(n1[1])
m=int(n2[0])
n=int(n2[1])

if(y>n):
    if(y%n==0):
        max_d=y
        m=m*(max_d/n)
    else:
        max_k=y%n #y,n最大公因數
        max_d=max_k*(y/max_k)*(n/max_k) #y,n最小公倍數
        x=x*(max_d/y)
        m=m*(max_d/n)
    p=x+m
    q=max_d
elif(y<n):
    if(n%y==0):
        max_d=n
        x=x*(max_d/y)
    else:
        max_k=n%y #y,n最大公因數
        max_d=max_k*(y/max_k)*(n/max_k) #y,n最小公倍數
        x=x*(max_d/y)
        m=m*(max_d/n)
    p=int(x+m)
    q=int(max_d)
else:
    p=x+m
    q=y
x=int(x)

def compute(a,b):
    while(b!=0):
        c=a%b
        a=b
        b=c
    return a
s=compute(p,q)
p=int(p/s)
q=int(q/s)
print(str(x)+' / '+str(y)+' + '+str(m)+' / '+str(n)+' = '+str(p)+' / '+str(q))

'''

'''5-6
m1=input("請輸入第1個矩陣的四個數字(每數字要換行):\n")
m1=list(m1)
for i in range(0,3,1):
    m3=list(input())
    m1=m1+m3

m2=input("請輸入第2個矩陣的四個數字(每數字要換行):\n")
m2=list(m2)
for i in range(0,3,1):
    m4=list(input())
    m2=m2+m4

print('Matrix1:\n'+str(m1[0])+'\t'+str(m1[1])+'\n'+str(m1[2])+'\t'+str(m1[3]))
print('Matrix2:\n'+str(m2[0])+'\t'+str(m2[1])+'\n'+str(m2[2])+'\t'+str(m2[3]))

for j in range(0,4,1):
    m1[j]=int(m1[j])+int(m2[j])
print('sum of 2 Matrix:\n'+str(m1[0])+'\t'+str(m1[1])+'\n'+str(m1[2])+'\t'+str(m1[3]))
'''

'''5-7
sentence=str(input("請輸入一段英文句子："))
sentence=sentence.split(' ')
print(sentence, end=',')
print("length:"+str(len(sentence))) #原輸入的字串與長度
sent_complete=sentence.copy() #設sent_complete跟原輸入一樣的串列

sentence=set(sentence) #用set去掉重複字 sentence從串列變成set
print(sentence, end=',')
print("length:"+str(len(sentence))) #去掉重複字後的字串與長度

sentence_copy=sentence.copy() #sentence與sentence_copy都是set不含重複字
c=[]
for i in range(0, len(sentence),1):
    c.append('0')

new_sent=c.copy() #new_sent與c串列用來記錄各個單字的encode
for i in range(0,len(sentence),1):
    c[i]='1'
    new_sent[i]=str(c)
    c[i]='0'

print("*Look Up Table:")
k=0
for i in sentence_copy:
    print("-"+str(i), end='\t')
    print(new_sent[k])
    c[k]=i
    k+=1

print("*Encoding Result:")
for i in range(0,len(sent_complete),1):
    print(sent_complete[i], end='\t')
    for j in range(0,len(c),1):
        if(sent_complete[i]==c[j]):
            sent_complete[i]=new_sent[j]
            print(sent_complete[i]) 

'''

