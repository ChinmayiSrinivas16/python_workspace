import re


us_pattern = r'^(?:\+1\s?)?(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$'
indian_pattern = r'^(?:\+91[\-\s]?)?[6-9]\d{9}$'


phone_number = input("Enter phone number: ")

if re.match(us_pattern, phone_number):
    print("Valid US phone number:", phone_number)
elif re.match(indian_pattern, phone_number):
    print("Valid Indian phone number:", phone_number)
else:
    print("Invalid phone number format")
