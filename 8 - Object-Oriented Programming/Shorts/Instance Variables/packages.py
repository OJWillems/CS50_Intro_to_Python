class Package:
    def __init__(self, package_id, sender, recipient, weight):
        self.package_id = package_id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 25)
    ]
    for package in packages:
        print(f"Package {package.package_id}: {package.sender} to {package.recipient}, {package.weight}kg")

if __name__ == "__main__":
    main()