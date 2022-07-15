'''
This program checks the validity of an inputted IPv4 address.
Author: J. Bottorff 07/15/22
'''

def addressNumeric(addr_list):
    for octet in addr_list:
        if octet.isnumeric() == False:
            return False
    else:
        return True

def addressLength(addr_list):
    if len(addr_list) == 4:
        return True
    else:
        return False

def leadingZero(addr_list):
    for octet in addr_list:
        if len(octet) > 1:
            if octet.startswith('0'):
                return False
    else:
        return True

def addressRange(addr_list):
    for octet in addr_list:
        if 0 <= int(octet) <= 255:
            continue
        else:
            return False
    else:
        return True

def invalid_msg(addr):
    print(addr, "is not a valid IPv4 address.")

print('Welcome to the IPv4 Address Validator.')
while True:
    addr = input('Enter an IPv4 address, or q to quit: ')
    #Convert input to a list
    addr_list = addr.split(".")
    #Exit if 'q' entered
    if addr == 'q':
        print('Exiting program.')
        break
    #Check if address entered is numeric
    elif addressNumeric(addr_list) == False:
        invalid_msg(addr)
    #Check if address entered has 4 octets
    elif addressLength(addr_list) == False:
        invalid_msg(addr)
    #Check if address has leading 0's
    elif leadingZero(addr_list) == False:
        invalid_msg(addr)
    #Check if address is in correct range
    elif addressRange(addr_list) == False:
        invalid_msg(addr)
    #If address passes the above tests, consider it valid
    else:
        print(addr, "is a valid IPv4 address.")
