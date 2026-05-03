a=open("data.txt","r+")
print(a.read())

a.write(" \n 4 to ka one ")
print(a.read())
a.close()
print("data written succensfully ")
