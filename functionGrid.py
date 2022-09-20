#desenha uma grade 4x4
def first_print():
    print('+','-','-','+')
def second_print():
    print('|',' ',' ','|')
def do_twice(f):
    f()
    f()
first_print()
do_twice(second_print)
first_print()

    
