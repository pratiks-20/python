n=8  #int(input("Enter a number"))

a=n*n
v=1

for _ in range(100):
    if(v>a):
        break;
    else:
        print (v)
        v*=2