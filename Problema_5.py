with open('numar.txt', 'r') as f:
    n = f.readline()
i=0
for i in range(1, 11):
    with open ('inmultire.txt', 'w') as f:
        f.write(str(i))
        f.write('*')
        f.write(n)
        f.write('=')
        p=i*int(n)
        f.write(str(p))
        f.write('   ')
