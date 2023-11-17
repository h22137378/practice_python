a=int(input("input a:"))
b=int(input("input b:"))
operator=input("input an operator (+,-,*,/):")

if operator=='+':
    print("a+b="+str(a+b))
elif operator=='-':
    print("a-b="+str(a-b))
elif operator=='*':
    print("a*b="+str(a*b))
else:
    print("a/b="+str(a/b))

'''
a = int(input('input a: '))
b = int(input('input b: '))
op = input('input a operator (+,-,*,/): ')
op_dict = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
print(f'a {op} b = {op_dict[op]}')
'''