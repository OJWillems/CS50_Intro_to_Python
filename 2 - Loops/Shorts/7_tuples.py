import sys

def main():
    # TUPLE:
    coordinates = (42.376, -71.115)

    print(coordinates)
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

    print("BREAK")

    # You're initializing two new variables - latitude and longitude - and assigning their values to the values of the coordinates tuple in order
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    print("BREAK")

    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
    # Because tuples are immutable, they take up less space than lists, which have to consider the possibility of being changed

main()