from TextSearch import *
from time import *

# len_sub_1, len_text_1 = len('adb'), len('adadadadadb')
# len_sub_2, len_text_2 = len('yoyololo'), len('yoyoyoloyoloyoyololo')
# len_sub_3, len_text_3 = len('nonono'), len('mononomononomonomononono')

start = time()
print pys('adb', 'adadadadadb'),
print pys('yoyololo', 'yoyoyoloyoloyoyololo'),
print pys('nonono', 'mononomononomonomononono'),
print pys('adb', 'adadadadadb'),
print pys('yoyololo', 'yoyoyoloyoloyoyololo'),
print pys('nonono', 'mononomononomonomononono'),
print pys('adb', 'adadadadadb'),
print pys('yoyololo', 'yoyoyoloyoloyoyololo'),
print pys('nonono', 'mononomononomonomononono'),
print pys('adb', 'adadadadadb'),
print pys('yoyololo', 'yoyoyoloyoloyoyololo'),
print pys('nonono', 'mononomononomonomononono')
print time() - start

start = time()
print sts('adb', 'adadadadadb'),
print sts('yoyololo', 'yoyoyoloyoloyoyololo'),
print sts('nonono', 'mononomononomonomononono'),
print sts('adb', 'adadadadadb'),
print sts('yoyololo', 'yoyoyoloyoloyoyololo'),
print sts('nonono', 'mononomononomonomononono'),
print sts('adb', 'adadadadadb'),
print sts('yoyololo', 'yoyoyoloyoloyoyololo'),
print sts('nonono', 'mononomononomonomononono'),
print sts('adb', 'adadadadadb'),
print sts('yoyololo', 'yoyoyoloyoloyoyololo'),
print sts('nonono', 'mononomononomonomononono')
print time() - start

start = time()
print kmp('adb', 'adadadadadb'),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo'),
print kmp('nonono', 'mononomononomonomononono'),
print kmp('adb', 'adadadadadb'),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo'),
print kmp('nonono', 'mononomononomonomononono'),
print kmp('adb', 'adadadadadb'),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo'),
print kmp('nonono', 'mononomononomonomononono'),
print kmp('adb', 'adadadadadb'),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo'),
print kmp('nonono', 'mononomononomonomononono')
print time() - start

'''
print kmp('adb', 'adadadadadb', len_sub_1, len_text_1),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo', len_sub_2, len_text_2),
print kmp('nonono', 'mononomononomonomononono', len_sub_3, len_text_3),
print kmp('adb', 'adadadadadb', len_sub_1, len_text_1),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo', len_sub_2, len_text_2),
print kmp('nonono', 'mononomononomonomononono', len_sub_3, len_text_3),
print kmp('adb', 'adadadadadb', len_sub_1, len_text_1),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo', len_sub_2, len_text_2),
print kmp('nonono', 'mononomononomonomononono', len_sub_3, len_text_3),
print kmp('adb', 'adadadadadb', len_sub_1, len_text_1),
print kmp('yoyololo', 'yoyoyoloyoloyoyololo', len_sub_2, len_text_2),
print kmp('nonono', 'mononomononomonomononono', len_sub_3, len_text_3)
'''
