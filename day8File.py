#  FILE HANDLING 


#  r for read 
# w for write only 
#  a for append and write at last
# x for creating new file and writing
# b binary mode
# t for text mode 
# open disk 


# myFile = open("app.txt","a")

# # data = myFile.readline()
# # # data = myFile.read() whole file 
# # data = myFile.readlines()

# # print(data)

# myFile.write("\n my hello")
# # myFile.writelines("")
# # print(ans)
# # print(data)
# myFile.close()

def replace1(file,old,new,newfile,mode):
    myfile = open(file,mode)
    if mode =="r":
       data = myfile.read()
       loc = data.find("everyone")
       print(loc)
       d= data.replace(old,new)
       print(d)
    # myfile.write("he everyone my name is javascript")
    elif mode=="w":
      myfile.write(d)
    myfile.close()

replace1("demo.txt","python","javascript","new.txt","r")