import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code: ")

try:
    phone = phonenumbers.parse(number, None)

    print("Valid:", phonenumbers.is_valid_number(phone))
    print("Country:", geocoder.description_for_number(phone, "en"))
    print("Number type:", phonenumbers.number_type(phone))
    print("Carrier:", carrier.name_for_number(phone, "en"))

except phonenumbers.NumberParseException as error:
    print("Invalid number:", error)