#assignment4
#task1
# WAP to take user input and writes it to a file named output.txt.
# appends additional data to the same file.
# reads and displays the final content of the file.
first_input = input("enter text to write to the file: ")
file1 = open("output.txt","w")
file_writing = file1.write(first_input + "\n")
file1.close()

second_input = input("enter additional text to append: ")
file2 = open("output.txt","a")
file2_writing = file2.write(second_input)
file2.close()

file1 = open("output.txt","r")
file_reading = file1.read()
file1.close()
print("Final content of output.txt: ",file_reading)



















