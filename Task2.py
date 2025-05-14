# Write and Append Data to a File

data = input("Enter text to write to the file: ")
file1 = open('output.txt', 'w')
file1.write(data)
print('Data successfully written to output.txt.\n')
file1.close()


data_for_append = input('Enter additional text to append: ')
file1 = open('output.txt', 'a')
appending_file = file1.write('\n' + data_for_append)
print('Data successfully appended.\n')
file1.close()


file1 = open('output.txt', 'r')
reading_file = file1.read()
print('Final content of output.txt:\n',reading_file)
file1.close()
