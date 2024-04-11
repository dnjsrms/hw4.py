def rep_char(c, n) :
    print(c * n)

def draw_line_string(name) :
    msg1= f'  Hello {name}'
    msg2 = ' Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr  +1)
    print(f'{msg1}, \n {msg2}')
    rep_char('-', nstr  +1)


name = input('input his/her name: ')
draw_line_string(name)
