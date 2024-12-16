try:
    myfile = open("mytext.txt","wt")
    for i in range(10):
        myfile.write("line #" + str(i+1) + "\n")
    myfile.close()
except IOError as error:
    print("The error is"+str(error))