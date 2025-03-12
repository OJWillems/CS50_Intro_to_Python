def main():
    guest_list = ["Mario", "Luigi", "Daisy", "Yoshi"]

    # for i in range(len(guest_list)):
    for guest in guest_list:
        print(write_letter(guest, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
        +-------------------------------------+
        Dear {receiver},

        You are coridally invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
        +-------------------------------------+
        """

main()