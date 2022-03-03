all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def validate_pin(pin):

  if len(pin) != 4 and len(pin) != 6:
    return False
  for s in pin:
    if s not in all_digits:
        return False
  return True

pins = ['1234', '678435', '7452', 'aj475']

#print(validate_pin(pins)) 