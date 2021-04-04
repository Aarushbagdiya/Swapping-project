def SwapFileData ():
    file1=input('Enter File Name')
    file2=input('Enter FIle Name')
    with open(file1,'r') as ab:
    x = ab.read()
    with open(file2,'r') as cd:
    y = cd.read()
      
    with open(file1,'w') as ab:
    ab.write(x)
    with open(file2,'w') as cd:
    cd.write(y)
SwapFileData ():     