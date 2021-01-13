with open('numere.txt', 'r') as f:
    a = f.readline()  
    b = f.readline()

if a>b:
    with open('produs.txt', 'w') as f:
        x=int(a)*2
        y=int(b)*3
        f.write(str(x))
        f.write('     ')
        f.write(str(y))
    
if a<b:
    with open('produs.txt', 'w') as f:
        y=int(b)*2
        x=int(a)*3
        f.write(str(x))
        f.write('     ')
        f.write(str(y))