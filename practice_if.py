'''2-1
x=input("請輸入第一個數：")
y=input("請輸入第二個數：")
if(x>y):
    print(x)
elif(y>x):
    print(y)
else:
    print('equal')
'''

'''2-2
x=float(input("請輸入第一個數："))
y=float(input("請輸入第二個數："))
if(x>y):
    x=x-y
    print(x)
elif(x<y):
    y=y-x
    print(y)
else:
    print(0)
'''

'''2-3
age=int(input("請輸入年齡："))
if(age<18):
    print("不能投票")
else:
    print("可以投票")
'''

'''2-4
python=input("請輸入一字串：")
if(python=='python'):
    print("hello "+python)
elif(python=='Python'):
    print("hello "+python)
else:
    print("錯頻囉～")
'''

'''2-5
score=int(input("請輸入成績："))
if(score>=90):
    print("A")
elif(score>=80 and score<=89):
    print("B")
elif(score>=70 and score<=79):
    print("C")
elif(score>=60 and score<=69):
    print("D")
else:
    print("F")
'''

'''2-6
price=int(input("請輸入金額："))
if(price>=10000):
    dis=price*0.7
    print(dis)
elif(price<10000 and price>=5000):
    dis=price*0.8
    print(dis)
elif(price<5000 and price>=1000):
    dis=price*0.9
    print(dis)
else:
    print(price)
'''