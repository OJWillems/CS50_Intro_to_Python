def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            # .pop() removes the last item from a list
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            # Clear a list
            history.clear()
        else:
            history.append(action)

        print(history)


main()