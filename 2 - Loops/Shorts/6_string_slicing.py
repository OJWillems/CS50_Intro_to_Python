def main():
    phone = "617-495-1000"

    print(phone)

    # Area code, index 0 INCLUSIVE : index 3 EXCLUSIVE
    print(phone[0:3])

    # If you leave the first digit blank, Python will assume it's index 0
    print(phone[:3])

    # Last four digits: 
    # BAD:
    print(phone[8:12])
    # BETTER:
    print(phone[8:])
    # BEST:
    print(phone[-4:])

main()