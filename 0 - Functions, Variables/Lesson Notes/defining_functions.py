def main():
    sanitized_name = input("What's your name? ").strip().title()
    hello(sanitized_name)

def hello(name="world"):
    print("Hello,", name)


hello()

main()