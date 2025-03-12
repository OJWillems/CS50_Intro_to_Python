class Package:
    def __init__(self, package_id, sender, recipient, weight):
        self.package_id = package_id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(package_id=2, sender="Bob", recipient="Charlie", weight=25)
    ]
    print(packages[1].sender)

if __name__ == "__main__":
    main()