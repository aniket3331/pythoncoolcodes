from itertools import product
x=list(map(int,input().split()))   
y=list(map(int,input().split()))           
a=list(product(x,y))
for i in a:
    print(i,end=' ')