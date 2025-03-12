import re
import sys

def main():
    ip_input = input("IPv4 Address: ")
    print(validate(ip_input))

def validate(ip):
    pattern = r"^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"
    if re.search(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()