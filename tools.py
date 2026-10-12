def validate_code (PIN):
    if len (PIN) == 4:
        return True
    else:
        print ("PIN must be 4 characters")
        return False

def is_a_number (PIN):
    if PIN.isdigit () == True:
        return True
    else:
        return False