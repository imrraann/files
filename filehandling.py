import os
print(os.getcwd())
f=open("tet.txt",'w')
f.write("I am imran")
f.close()

#to show all list of directories
print(os.listdir())
 #using for loop
file=os.listdir()
for files in file:
    print(files)
print(len(file))