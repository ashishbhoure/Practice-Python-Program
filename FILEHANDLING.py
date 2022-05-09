f=open("Myfirstfile.txt","w")
    x="HELLO"
    f.write(x)
    y="ASHISH BHOURE"
    f.write("\n"+y)
#f.write(y)
f.close()

#read file

f=open("Myfirstfile.txt","r")
    x=f.read()
    print(x)
f.close()
