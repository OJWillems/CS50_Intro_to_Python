# With Validator-Collection

from validator_collection import validators, checkers, errors

def main():
    email_input = input("What's your email address? ").strip()
    print(check_email(email_input))

def check_email(string):
    if checkers.is_email(string):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()

# With Validators

# import validators

# def main():
#     email_input = input("What's your email address? ").strip()
#     print(check_email(email_input))

# def check_email(string):
#     try:
#         if validators.email(string, r_ve=True):
#             return "Valid"
#     except validators.ValidationError:
#         return "Invalid"

# if __name__ == "__main__":
#     main()