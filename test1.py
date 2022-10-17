def readFile(filename):
    """file name with.txt format """
    f=open(filename,"r")
    x=[f.read()][0].split()
    x2=[]
    for i in x:
        x2.append(int(i))
    return x2


def common_element(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3


def writeFile(filename,l3):
    """filename with .txt format"""
    f=open(filename,"w")
    for i in l3:
        f.write("%s\n"%i)
    f.close()

a=readFile("primenumbers.txt")
b=readFile("primenumbers.txt")
c=common_element(a,b)
writeFile("common_numbers.txt",c)