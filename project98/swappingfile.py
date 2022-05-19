#  c:/Users/vishnu/Desktop/VishnuFolder/Whitehat.Jr/Python Whitehat/project98/file1.txt
#  c:/Users/vishnu/Desktop/VishnuFolder/Whitehat.Jr/Python Whitehat/project98/file2.txt

def swapFileData():
    file1=input("Enter file 1 name to swap:-")
    file2=input("Enter file 2 name to swap:-")
     
    with open(file1,'r') as a:
      data_a = a.read()
    with open(file2,'r') as b:
       data_b=b.read()
    with open(file1,'w') as c:
        c.write(data_b)
    with open(file2,'w') as d:
        d.write(data_a)

swapFileData()