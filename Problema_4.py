with open('input.txt', 'r') as f:
    a = f.readline()  
pp=int(a)-2
p=pp+1
s=int(a)+1
ss=s+1
with open('output.txt', 'w') as f:
    f.write(str(pp))
    f.write(',')
    f.write(str(p))
    f.write(',')
    f.write(a)
    f.write(',')
    f.write(str(s))
    f.write(',')
    f.write(str(ss))