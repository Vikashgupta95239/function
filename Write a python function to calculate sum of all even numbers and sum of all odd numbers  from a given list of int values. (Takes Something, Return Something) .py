def evansum(n):
    s=0
    for x in n:
        if x%2==0:
            s=s+x
    return(s)
def oddsum(n):
    s=0
    for x in n:
        if x%2!=0:
            s=s+x
    return(s)
l=[int(x) for x in input("enter the number with comma separate").split(",")]
y=evansum(l)
z=oddsum(l)
print("evan sum {}\nod sum {}".format(y,z))