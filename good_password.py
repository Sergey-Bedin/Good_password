def is_password_good(password):
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if len(password) >= 8:
        flag1 = True
    for c in password:
        if c.isalpha():
            if c == c.upper():
                flag2 = True
            elif c == c.lower():
                flag3 = True
        if c.isdigit():
            flag4 = True
    return flag1 and flag2 and flag3 and flag4


txt = input()


print(is_password_good(txt))
