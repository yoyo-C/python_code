from sys import argv
import operator

if len(argv) <= 3:
    print "Usage: python homework2.py [input_file] [output_file1] [output_file2]"
    sys.exit(1)

input_file,output_file1, output_file2 = argv[1], argv[2], argv[3]

input_fd = open(input_file)
input_fd.readline()

lessons = ['HT', 'PT','MT','HY','MY']
lesson_number = {'RF': 0, 'Python': 0,'CASE': 0,'KeywordsRunner': 0,'Selenium': 0}
group = raw_input("Enter the group you are in: ").upper()

while not group in lessons:
    print "The group you enter is not in the list."
    group = raw_input("Enter the group you are in, Again: ").upper()

namelist_in_mygroup = []

while True:

    lesson_record = input_fd.readline().strip()

    if lesson_record == '':
        input_fd.close()             
        break

    lesson_record_list = lesson_record.split(',')

    if lesson_record_list[0] == group:
        namelist_in_mygroup.append(lesson_record_list[1])

        if lesson_record_list[2] == '1':
            lesson_number['RF'] += 1

        if lesson_record_list[3] == '1':
            lesson_number['Python'] += 1

        if lesson_record_list[4] == '1':
            lesson_number['CASE'] += 1

        if lesson_record_list[5] == '1':
            lesson_number['KeywordsRunner'] += 1

        if lesson_record_list[6] == '1':
            lesson_number['Selenium'] += 1
 

sorted_lesson_number = sorted(lesson_number.items(), key = operator.itemgetter(1))

print "\tNumbers of people in the five lessons: ", sorted_lesson_number
print "\tPeople who are in the same group with you: ", namelist_in_mygroup

output1_fd = open(output_file1, 'w')
str_lesson_number = str(sorted_lesson_number)
output1_fd.write(str_lesson_number)
output1_fd.close()

your_name = raw_input("Enter your name in PinYin: ").lower()

while not your_name in namelist_in_mygroup:
    print "Your name is not in the list."
    your_name = raw_input("Enter your name in Pinyin again: ").lower()
    
for i in range(len(namelist_in_mygroup)):

    if your_name == namelist_in_mygroup[i]:
        del namelist_in_mygroup[i]
        break

output2_fd = open(output_file2, 'w')
str_namelist = str(namelist_in_mygroup)
output2_fd.write(str_namelist)
output2_fd.close()



