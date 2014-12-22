my_list = [i**2 for i in range(1,11)]

input_fd = open("hello.txt", 'w')

for i in my_list:
    input_fd.write(str(i) + '\n')

input_fd.close()
