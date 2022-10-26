def lcm(a,b):
    for i in range(1,a*b,1):
    # i=1
    # while(i<=a*b):
        if(i%a==0 and i%b==0):
            break
        i+=1
    print("lcm =",i)
             
lcm(4,5)
    
