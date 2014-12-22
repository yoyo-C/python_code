from sys import argv
file_myhw, file_stdhw = argv[1], argv[2]

myhw_hd = open(file_myhw, 'r')
stdhw_hd = open(file_stdhw,'r')

myhw_read = myhw_hd.read()
stdhw_read = stdhw_hd.read()
