from tkinter import N


price=int(input("price:"))
sale=input("on sale?(y/n):")

if sale == 'y':
    discount = float(input('discount? (float): '))
    print(f'price = {price * discount}')
else: 
    print(f'price = {price}')
'''
if sale=='n' or 'N':
    print("price:"+str(price))
if sale=='y' or 'Y':
    discount=float(input("discount?(float):"))
    print("price:"+str(price*discount))
'''