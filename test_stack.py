import math
import LinearStructures

data_list = []
for p in xrange(6):
    data_list.append(p)

print data_list

my_list = LinearStructures.Stack()
my_list.print_list()
my_list.push(data_list[0])
my_list.print_list()
my_list.push(data_list[1])
my_list.print_list()
my_list.push(data_list[2])
my_list.print_list()
print my_list.pop()
print my_list.peek()
my_list.print_stack()
