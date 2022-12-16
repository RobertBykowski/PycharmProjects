import re
def is_valid_phone_number(phone_number):
    # Use a regex to check if the phone number is in the correct format
    pattern = r'\d{3}-\d{3}-\d{3}'
    if re.match(pattern, phone_number):
        return True
    return False
