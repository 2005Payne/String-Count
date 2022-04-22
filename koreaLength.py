a=[]
count=0
while(True):
    b=list(input())
    if(b==['*']):
        break
    a+=b
for i in range(len(a)):
    if(a[i]!=' 'and a[i]!='.' and a[i]!=','):
        count+=1
print(count)