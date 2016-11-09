from Trees import *

data_list = []
for p in xrange(16):
    data_list.append(p)

print data_list

my_tree = BinarySearchTree()
print my_tree.is_empty()
my_tree.set_root(TreeNode(data_list[8]))
print "Assert\t",
print my_tree.get_root().get_data() == data_list[8]
print "Weights\t",
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[4])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[2])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[1])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[3])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[5])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[6])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[7])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[12])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[10])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[9])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[11])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[15])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[14])
print my_tree.get_root().get_weight(),
my_tree.insert(data_list[13])
print my_tree.get_root().get_weight()
'''
            +---------------8----------------+  
    +-------4---+                    +------12-----------+
+---2---+       5---+           +---10---+           +--15
1       3           6---+       9       11       +--14
                        7                       13
'''
print "Inorder\t",
my_tree.print_in_order()
print

# 1
node = my_tree.get_root().get_left().get_left().get_left()
print "Successor of root with data = %d is node with data = %d" % (
node.get_data(), node.get_successor().get_data())

# 7
node = my_tree.get_root().get_left().get_right().get_right().get_right()
print "Successor of root with data = %d is node with data = %d" % (
node.get_data(), node.get_successor().get_data())

# 8
node = my_tree.get_root()
print "Successor of root with data = %d is node with data = %d" % (
node.get_data(), node.get_successor().get_data())

# 15
node = my_tree.get_root().get_right().get_right()
print "Successor of root with data = %d is node with data = %d" % (
node.get_data(),
-1 if node.get_successor() == None else node.get_successor())

for i in xrange(0, 32, 5):
    print i, my_tree.contains(i),
print

my_tree.delete(11)
# my_tree.delete(12)
my_tree.delete(15)

print "Inorder\t",
my_tree.print_in_order()
print
