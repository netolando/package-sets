import os
import time


def get_list(input_file): #gets a file and turns it into a list
    with open(input_file,'r') as f:
        file_list = [x.rstrip() for x in f.readlines()]
        return file_list

def build_list(input_list,output_file): #creates a file from a list
    with open(output_file,'a') as f:
        for item in input_list:
            if 'DEC' in item:
                f.write(item + '\n')


list_a = 'file_a.txt'
list_b = 'file_b.txt'

set_a = set(get_list(os.path.join('./input',list_a)))
set_b = set(get_list(os.path.join('./input',list_b)))

set_c = set_a - set_b

output_file = os.path.join('./output',time.strftime("%Y%m%d_%H%M%S")+'.txt')

build_list(list(set_c),output_file)
print('Done')