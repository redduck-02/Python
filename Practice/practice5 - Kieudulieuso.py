#Type
d=4
print(type(d))
e=4.5
print(type(e))
f="abc"
print(type(f))

#Decimal
from decimal import*
getcontext().prec=30

a=10/3
print(a)
print(type(a))
b=Decimal(10)/Decimal(3)
print(b)
print(type(b))

#Phân số
from fractions import*
frac=Fraction(6/3)
print(frac)
print(type(frac))

frac1=Fraction(6/2)
frac2=Fraction(6/4)
frac3= frac1 + frac2
print(frac3)

#Số phức
c= complex(2,5)
print(c)
#Lấy phần thực
print(c.real)
#Lấy phần ảo
print(c.imag)