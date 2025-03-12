class Ingredient:
    def __init__(self, name, hearts):
        self.name = name
        self.hearts = hearts

class Dish:
    base_hearts = 1

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.hearts = Dish.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            hearts += ingredient.hearts
        return hearts
    
    # def calculate_hearts(self, ingredients):
    #     hearts = self.base_hearts
    #     for ingredient in ingredients:
    #         hearts += ingredient.hearts
    #     return hearts

def main():
    ingredients = gather_ingredients()
    dish = cook_dish(ingredients)
    print(f"You cooked a {dish.name}! Eat it to heal {dish.hearts} hearts.")

def gather_ingredients():
    ingredients = []
    while True:
        try:
            name = input("Ingredient name: ")
            hearts = int(input("Number of hearts: "))
        except KeyboardInterrupt:
            print("")
            return ingredients
        else:
            ingredients.append(Ingredient(name, hearts))
        
def cook_dish(ingredients):
    return Dish(input("Dish Name: "), ingredients)
    
if __name__ == "__main__":
    main()