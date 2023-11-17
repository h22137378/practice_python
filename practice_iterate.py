'''3-1
n=int(input("請輸入一整數："))
for i in range(n,0,-1):
    print('"'+str(i)+'"', end='')
'''

'''3-2
name=input("請輸入名字：")
for j in range(0,2):
    for i in range(0, len(name), 1):
        print(name[i], end='')
'''

'''3-3
#方法一
i=1
while(i<=100):
    if(i%2==0):
        print(i, end=' ')
    i+=1

#方法二
for i in range(2,101,2):
    print(i, end=' ')
'''

'''3-4
for i in range(1,21,1):
    print(i,end=' ')
'''

'''3-5
#方法一
i=1
while(i<=100):
    if(i%2==1):
        print(i, end=' ')
    i+=1

#方法二
for i in range(1,101,2):
    if(i%2==1):
        print(i, end=' ')
'''

'''3-6
x=int(input("請輸入第一個整數："))
y=int(input("請輸入第二個整數："))
if(x>y):
    i=x
else:
    i=y
while(i%x!=0 or i%y!=0):
    i+=1
print(i)
'''

