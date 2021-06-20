#Đổi 2 giá trị a b cho nhau

#Cho b=a
a = 1
b = 2

print("a = " + str(a))
print("b = " + str(b))

b = a

print("---")
print("a = " + str(a))
print("b = " + str(b)) #=> không dùng được

#Dùng temp
c = 1
d = 2

print("---")
print("c = " + str(c))
print("d = " + str(d))

temp = c
c = d
d = temp

print("---")
print("c = " + str(c))
print("d = " + str(d))