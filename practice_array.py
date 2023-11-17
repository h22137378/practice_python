'''4-1
x=['kiwi','coconut','lemon','guava','mengo']
print(x[2])
'''

'''4-2
tuple=('bread','milk','eggs')
t=list(tuple)
print(t)
t.append('apple')
print(t)
'''

'''4-3
tuple=('bread','milk','eggs','apple')
t=list(tuple)
t.insert(2,'ham')
print(t)
'''

'''4-4
math_pass=['小新','美冴','風間','妮妮','娜娜子姊姊']
eng_pass=['小白','廣志','正男','阿呆','園長','動感超人']
a=set(math_pass).difference(eng_pass)
b=set(eng_pass).difference(math_pass)
print(str(a)+'\n'+str(b))
'''

'''4-5 不確定
title='name','age','depart'
name='John Mckee','Lisa Crawford','Sujan Patel'
age='38','29','33'
depart='sales','Marketing','HR'
employee=list(zip(name, age, depart))
print(employee)
for i in range(0,len(title),1):
    print("第"+str(i+1)+"位員工資料："+str(employee[i]))
'''

