class Package:
    def __init__(self, package_id, sender, recipient, weight):
        self.package_id = package_id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.package_id}: {self.sender} to {self.recipient}, {self.weight}kg"
    
    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 25)
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")

if __name__ == "__main__":
    main()