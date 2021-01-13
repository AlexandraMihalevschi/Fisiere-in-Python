with open('numere.txt', 'r') as f:
    a = f.readline()  
    b = f.readline()

if a>b:
    with open('minim.txt', 'w') as f:
        f.write(b)
    
if a<b:
    with open('minim.txt', 'w') as f:
        f.write(a)