import string
string.ascii_uppercase
string.ascii_lowercase
src_str = string.ascii_uppercase
dst_str = src_str[1:] + src_str[:1]
print('dst_str = ', dst_str)
src_str.index('A')
n = src_str.index('A')
print('src_str의 A 인덱스 =', n)
