def prime(n):
    for i in range(2,n+1):
        k=0
        for j in range(2,i):
            if(i%j==0):
                k+=1
        if(k==0):
            print(i,end="\t")
print("enter the number ")
n=int(input())
prime(n)