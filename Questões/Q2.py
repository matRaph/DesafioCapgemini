
def secure_password(password):
    if len(password) == 0:
        return(6)
    elif len(password) == 1:
        return(5)
    elif len(password) == 2:
        return(4)
    elif len(password) == 3:
        return(3)
    elif len(password) > 3:
        condit_remaining = 4
        new_password = password
        if any(chr.isdigit() for chr in password):
            new_password = ''.join([i for i in new_password if not i.isdigit()])
            condit_remaining = condit_remaining - 1
        if any(chr.isupper() for chr in password):
            new_password = ''.join([i for i in new_password if not i.isupper()])
            condit_remaining = condit_remaining - 1
        if any(chr.islower() for chr in password):
            new_password = ''.join([i for i in new_password if not i.islower()])
            condit_remaining = condit_remaining - 1
        if len(new_password) > 0:
            condit_remaining = condit_remaining - 1
        if condit_remaining + len(password) >= 6:
            return(condit_remaining)
        elif len(password) == 4:
            return(2)
        else:
            return(1)

print(secure_password(str(input())))