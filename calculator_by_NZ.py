import tkinter as tk

window = tk.Tk()
window.title('Calculator by Niloofar Zolfigol')
window.resizable(width=False, height=False)

lbl_result = tk.Label(master=window, text='0', height=4, width=32,
                      font=("Arial", 12), fg="blue", bg='light grey')
lbl_result.grid(row=0, column=0, columnspan=4)


def insert_multiply_before_left_paren(current):
    """ 3(1+2) => 3*(1+2) """
    current = list(current)
    i = 0
    while i < len(current):
        if current[i] == '(' and (current[i-1] not in ['/', '+', '-', '*', '(']):
            current.insert(i, '*')
            i += 1
        i += 1
    if current[0] == '*':
        current.pop(0)
    current = ''.join(current)
    return current


def insert_multiple_after_rightparen_and_before_num(current):
    """ (1+2)3 => (1+2)*3 """
    if ')0' in current:
        current = current.replace(')0', ')*0')
    if ')1' in current:
        current = current.replace(')1', ')*1')
    if ')2' in current:
        current = current.replace(')2', ')*2')
    if ')3' in current:
        current = current.replace(')3', ')*3')
    if ')4' in current:
        current = current.replace(')4', ')*4')
    if ')5' in current:
        current = current.replace(')5', ')*5')
    if ')6' in current:
        current = current.replace(')6', ')*6')
    if ')7' in current:
        current = current.replace(')7', ')*7')
    if ')8' in current:
        current = current.replace(')8', ')*8')
    if ')9' in current:
        current = current.replace(')9', ')*9')
    if ').' in current:
        current = current.replace(').', ')*.')
    return current


def one_divide_to_num():
    """a function to calculate 1/x"""
    try:
        lbl_result['text'] = str(1/float(eval(lbl_result['text'])))
    except ZeroDivisionError:
        lbl_result['text'] = 'ZeroDivisionError\nPress Clear to reset!'


def sqr():
    """a function to calculate square root of x => x^(0.5)"""
    current = lbl_result['text']
    current = insert_multiple_after_rightparen_and_before_num(current)
    current = insert_multiply_before_left_paren(current)
    lbl_result['text'] = str(float(eval(current))**(0.5))


def power_two():
    """a function to calculate power two of x => x^2"""
    current = lbl_result['text']
    current = insert_multiple_after_rightparen_and_before_num(current)
    current = insert_multiply_before_left_paren(current)
    lbl_result['text'] = str(float(eval(current))**2)


def power_three():
    """a function to calculate power three of x => x^3"""
    current = lbl_result['text']
    current = insert_multiple_after_rightparen_and_before_num(current)
    current = insert_multiply_before_left_paren(current)
    lbl_result['text'] = str(float(eval(current))**3)


def del_func(*args):
    """a function to delete the unexpectedly entered character"""
    if len(lbl_result['text']) != 1:
        lbl_result['text'] = lbl_result['text'][:-1]
    else:
        lbl_result['text'] = '0'


def is_decimal(current):
    """a function to check if a number is decimal or not"""
    for char in current[::-1]:
        if char == '.':
            return True
        if char in ['+', '-', '*', ')', '(']:
            return False
    return False


def remove_unnecessary_zero(current):
    """ a function to remove zero before integers (which will cause trouble for eval()) 2+01 => 2+1 """
    if current[-1] == '0' and len(current) == 1:  # if current is zero, do nothing.
        return current
    elif current[-1] == '0' and current[-2] in ['+', '-', '*', '/', '(', ')']:
        current = current.rstrip('0')
        return current
    return current


def insert_number_in_calc_result(btn_text):
    current = lbl_result['text']
    # clear the screen
    if btn_text == 'C':
        lbl_result['text'] = '0'
    elif current == '0':
        if btn_text == '.':
            lbl_result['text'] += btn_text
        else:
            lbl_result['text'] = btn_text
    elif btn_text == '.':
        if not is_decimal(current):
            lbl_result['text'] += btn_text
    # to avoid entring something like: +-
    elif btn_text in ['+', '-', '*', '/'] and (current[-1] in ['+', '-', '*', '/', '(']):
        lbl_result['text'] = current[:-1] + btn_text
    elif btn_text in ['(', ')']:
        lbl_result['text'] += btn_text
    elif btn_text == '=':
        print(current)  # uncomment to see behind the scene!
        current = insert_multiple_after_rightparen_and_before_num(current)
        current = insert_multiply_before_left_paren(current)
        try:
            lbl_result['text'] = f'{eval(current)}'
        except ZeroDivisionError:
            lbl_result['text'] = 'ZeroDivisionError\nPress Clear to reset'
    else:  # input is 0,1,2,3,4,5,6,7,8,9
        lbl_result['text'] = remove_unnecessary_zero(current) + btn_text


# list of options for Buttons
calc_keys = [
    {'text': '(',
     'command': lambda: insert_number_in_calc_result('(')},
    {'text': ')',
     'command': lambda: insert_number_in_calc_result(')')},
    {'text': '1/x',
     'command': one_divide_to_num},
    {'text': 'Delete',
     'command': del_func},
    {'text': 'sqr(x)',
     'command': sqr},
    {'text': 'x^2',
     'command': power_two},
    {'text': 'x^3',
     'command': power_three},
    {'text': '÷',
     'command': lambda: insert_number_in_calc_result('/')},
    {'text': '7',
     'command': lambda: insert_number_in_calc_result('7')},
    {'text': '8',
     'command': lambda: insert_number_in_calc_result('8')},
    {'text': '9',
     'command': lambda: insert_number_in_calc_result('9')},
    {'text': '+',
     'command': lambda: insert_number_in_calc_result('+')},
    {'text': '4',
     'command': lambda: insert_number_in_calc_result('4')},
    {'text': '5',
     'command': lambda: insert_number_in_calc_result('5')},
    {'text': '6',
     'command': lambda: insert_number_in_calc_result('6')},
    {'text': '-',
     'command': lambda: insert_number_in_calc_result('-')},
    {'text': '1',
     'command': lambda: insert_number_in_calc_result('1')},
    {'text': '2',
     'command': lambda: insert_number_in_calc_result('2')},
    {'text': '3',
     'command': lambda: insert_number_in_calc_result('3')},
    {'text': '*',
     'command': lambda: insert_number_in_calc_result('*')},
    {'text': '.',
     'command': lambda: insert_number_in_calc_result('.')},
    {'text': '0',
     'command': lambda: insert_number_in_calc_result('0')},
    {'text': 'Clear',
     'command': lambda: insert_number_in_calc_result('C')},
    {'text': '=',
     'command': lambda: insert_number_in_calc_result('=')},
]

calc_keys_objs = []
# building Buttons
for calc_key_data in calc_keys:
    btn = tk.Button(
        master=window,
        width=8,
        height=2,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        bg='light grey',
        font=('Calibri', 12)
    )
    calc_keys_objs.append(btn)

# showing buttons
for i, cal_key_obj in enumerate(calc_keys_objs):
    cal_key_obj.grid(row=((i//4) + 1), column=i % 4, sticky='nswe')

# ===================================================================================

# # uncomment codes below for a second calculator where you can type your calculations

# ent_typing_section = tk.Entry(width=32)
# lbl_typing_section = tk.Label(
#     width=24, text='Type your calculation above', height=2)


# def calc():
#     typ_sec_current = ent_typing_section.get()
#     typ_sec_current = insert_multiply_before_left_paren(typ_sec_current)
#     typ_sec_current = insert_multiple_after_rightparen_and_before_num(
#         typ_sec_current)
#     try:
#         lbl_typing_section['text'] = eval(typ_sec_current)
#     except SyntaxError:
#         lbl_typing_section['text'] = 'Enexpected Zero\ncheck and try again!'
#     except ZeroDivisionError:
#         lbl_typing_section['text'] = 'ZeroDivisionError\nReset'


# btn_calc = tk.Button(master=window, text='Calculate', command=calc, width=8,)
# ent_typing_section.grid(row=8, sticky='ewns', column=0, columnspan=4, )
# lbl_typing_section.grid(row=9, sticky='ewns', column=0, columnspan=3)
# btn_calc.grid(row=9, sticky='ewns', column=3)

# ===================================================================================
window.mainloop()
