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
        print ("PIN must be numbers")
        return False
    
def validate_account (account):
    if len(account) <=4:
        print ("Name account must contain 4 characters minimum")
        return False
    else:
        return True

   
   