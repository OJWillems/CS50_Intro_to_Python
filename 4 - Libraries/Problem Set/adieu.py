import inflect # type: ignore

inflection = inflect.engine()

def main():
    names_list = []
    while True:
        try:
            names_list.append(input("Name: "))
        except EOFError:
            print(f"Adieu, adieu, to {inflection.join(names_list)}")
            break

if __name__ == "__main__":
    main()