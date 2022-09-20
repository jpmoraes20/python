def do_twice(f,v):
    f(v)
    f(v)
def print_twice(bruce):
    print(bruce)
    print(bruce)
do_twice(print_twice,'spam')
print('\n')
def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')