try:
    file = open("1.txt","wt")
    for i in range(8):
        file.write("line " + str(i+1) + " of the file \n")
    file.close()
except IOError as error:
    print("The error is : " +str(error))