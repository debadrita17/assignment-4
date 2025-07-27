#assignment4
#task1
#WAP that open and reads a text  file named sample.txt
# print its content by line
# handles errors gracefully if the files does not exist.
try:
    file = open('sample.txt','w')
    writing_file = file.write('This is a sample text line. \n')
    writing_file1 = file.write(' It contains multiple lines')
    file.close()

    file = open('sample.txt','r')
    reading_file = file.readlines()
    print("From file1:",reading_file[0])
    print("From file2:", reading_file[1])
    file.close()

except FileNotFoundError:
    print("The error: The file 'sample.txt' was not found.")
finally:
    print("Finished reading/writing file. ")















