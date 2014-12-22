# coding: utf-8
from xpinyin import Pinyin 
import sys, locale
from sys import argv 

if len(argv) <= 2:
    print "Usage: python homework1.py [input_file] [output_file]"
    sys.exit(1)

input_file, output_file = argv[1], argv[2]
reload(sys)
sys.setdefaultencoding('utf-8')

def get_name(input_file, output_file):
    # get chinese name and transform into Pinyin
    print "Please enter your name in Chinese!"
    name_in_chinese = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
    p = Pinyin()  # create instance of Pinyin class
    name_in_pinyin = p.get_pinyin(name_in_chinese, '') # translate chinese into Pinyin and get rid of '-'

    input_fd = open(input_file) 
    input_fd.readline() # open file and read the first line

    lessons = [u"框架原理","Python", u"用例编写","Keywordsrunner", "Selenium"]
    total_lessons = len(lessons)
    line_num = 1  # count the row you are in

    while True:
        lesson_record = input_fd.readline().strip()
        lesson_record_list = lesson_record.split(',')
        line_num += 1

        if lesson_record == '':
            print "Cannot find your name."
            input_fd.close()
            return

        else:
            if lesson_record_list[1] == name_in_pinyin:
                print u"%s在第%d行，报名课程有:" % (name_in_chinese, line_num),
                context = u"%s在第%d行，报名课程有：" % (name_in_chinese, line_num)

                count = 0
                for i in range(total_lessons):
                    # Lesson fields started from 3rd column
                    if lesson_record_list[i + 2] == '1':
                        count += 1
                        print "%s," % lessons[i],
                        context = context + "%s, " % lessons[i]

                print u"总共%d课." % count
                context = context + u"总共%d课." % count
                input_fd.close()

                output_fd = open(output_file, 'wb')
                output_fd.write(context.encode('gbk'))
                output_fd.close()
                return

def learn_python_group(input_file, output_file):
    input_fd = open(input_file)
    input_fd.readline
    name = []
    group = []

    while True:
        member_record = input_fd.readline().strip()
        member_record_list = member_record.split(',')

        if member_record == '':
            break

        else:
            if member_record_list[3] == '1':
                name.append(member_record_list[1])
                group.append(member_record_list[0])

    print "The name list is:", name
    print "The group list is:", group
    input_fd.close()
    output_fd = open(output_file, 'a')
    name_str = str(name)
    group_str = str(group)
    output_fd.write(name_str)
    output_fd.write(group_str)
    output_fd.close()

    return name, group

def change_group(input_file, output_file):
    name, group = learn_python_group(input_file, output_file)
    get_name = raw_input("Enter your name in Pinyin: ")
 
    while not get_name in name:
        print "Your name is not in the list."
        get_name = raw_input("Enter your name in Pinyin, Again: ")

    group_to_change = raw_input("Enter the group you want to change to: ")

    for i in range(len(name)):
        if get_name == name[i]:
            group[i] = group_to_change

    print 'The changed name list is:', name
    print 'The changed group list is:', group

    output_fd = open(output_file, 'a')
    name = str(name)
    group = str(group)
    output_fd.write(name)
    output_fd.write(group)
    output_fd.close()

get_name(input_file, output_file)
change_group(input_file, output_file)