from jar import Jar

# jar_1 = Jar()
# print(f"Jar 1 Capacity: {jar_1.capacity}")
jar_1 = Jar(5)
print(f"Jar 1 Capacity: {jar_1.capacity}")

# jar_1.deposit(5)
# print(f"# of cookies in Jar 1: {jar_1.size}")
# print(jar_1)

# # THIS WILL BREAK IT:
# # jar_1.deposit(1)
# # print(f"# of cookies in Jar 1: {jar_1.size}")

# jar_1.withdraw(3)
# print(jar_1)
# print(f"# of cookies in Jar 1: {jar_1.size}")
# # jar_1.withdraw(2)
# # print(f"# of cookies in Jar 1: {jar_1.size}")
# jar_1.withdraw(1)

jar_1.size = 5
print(jar_1)
jar_1._size = 6
print(jar_1)

# print(f"# of cookies in Jar 2: {jar_2.size}")

# jar_1.deposit(1)
# jar_2.deposit(8)
# print(f"# of cookies in Jar 1: {jar_1.size}")
# print(f"# of cookies in Jar 2: {jar_2.size}")

