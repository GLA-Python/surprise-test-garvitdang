p=int(input("NUmber of terms you want"))
V=1
print(V)
while p>1:
    ans=""
    while V>0:
        c=V%10
        count=1
        V//=10
        while V>0 and V%10==c:
            count+=1
            V//=10
        ans=str(count)+str(c)+ans
    print(ans)
    V=int(ans)
    p-=1