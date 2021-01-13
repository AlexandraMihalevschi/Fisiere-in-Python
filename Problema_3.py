with open('globulete.txt', 'r') as f:
    a = f.readline()  

r = 3+int(a)
b = (r+int(a))-2
t = int(a)+r+b

with open('bradut.txt', 'w') as f:
    f.write(str(t))