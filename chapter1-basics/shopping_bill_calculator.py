a = input('Enter item 1 name: ')
p1 = int(input('Enter price:'))
b = input('Enter item 2 name: ')
p2 = int(input('Enter price:'))
c = input('Enter item 3 name: ')
p3 = int(input('Enter price:'))
print(f'''
===== BILL =====
{a}: ₹{p1}
{b}: ₹{p2}
{c}: ₹{p3}
-----------------
Subtotal: {p1+p2+p3}
GST (18%): {0.18*(p1+p2+p3)}
-----------------
TOTAL: ₹{1.18*(p1+p2+p3)}''')