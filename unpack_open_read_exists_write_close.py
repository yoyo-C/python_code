from sys import argv
script, input_file, output_file = argv

input_file_open = open(input_file)
input_file_read = input_file_open.read()
print input_file_read

output_file_open = open(output_file,'w+')
output_file_open.write(input_file_read)
print output_file_open.read()
output_file_open.close()
input_file_open.close()

