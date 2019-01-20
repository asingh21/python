import os
import re

dir = os.getcwd()
with open("try.txt") as file_obj:
    per_line_list = file_obj.readlines()
    for per_line in per_line_list:
        regex_obj = re.match(r'^(\D)(.*)', per_line)
        if regex_obj:
            print "regex_obj.group() = {}".format(regex_obj.group())
