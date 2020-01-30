def get_initial(name):
    return name[0:1].upper()

fn=input('Enter your first name: ')
mn=input('Enter your middle name: ')
ln=input('Enter your last name: ')

# 0 - Before creating the function get_initial()
# fn_i = fn[0:1]
# mn_i = mn[0:1]
# ln_i = ln[0:1]

# 1 - Before calling function inside the print statement
# fn_i = get_initial(fn)
# mn_i = get_initial(mn)
# ln_i = get_initial(ln)

# 0 - Before calling function inside the print statement
# 1 - print('Your initials are: ' + fn_i + mn_i + ln_i)
print('Your initials are: ' + get_initial(fn) + get_initial(mn) + get_initial(ln))