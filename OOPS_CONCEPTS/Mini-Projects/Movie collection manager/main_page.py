import json

movies = []


def load_movies():
    global movies

    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)

    except FileNotFoundError:
        movies = []


def save_movies():
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)


def add_movie():
    name = input("Enter movie name: ")
    genre = input("Enter genre: ")
    rating = float(input("Enter rating: "))

    movie = {
        "name": name,
        "genre": genre,
        "rating": rating
    }

    movies.append(movie)

    print("Movie added successfully!")


def view_movies():
    if not movies:
        print("No movies found.")
        return

    for movie in movies:
        print("-" * 30)
        print("Name:", movie["name"])
        print("Genre:", movie["genre"])
        print("Rating:", movie["rating"])


def search_movie():
    name = input("Enter movie name to search: ").lower()

    found = False

    for movie in movies:
        if movie["name"].lower() == name:
            print("\nMovie Found")
            print("Name:", movie["name"])
            print("Genre:", movie["genre"])
            print("Rating:", movie["rating"])
            found = True

    if not found:
        print("Movie not found.")


def delete_movie():
    name = input("Enter movie name to delete: ").lower()

    for movie in movies:
        if movie["name"].lower() == name:
            movies.remove(movie)
            print("Movie deleted successfully!")
            return

    print("Movie not found.")


load_movies()

while True:
    print("\n===== MOVIE COLLECTION MANAGER =====")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Delete Movie")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()

    elif choice == "2":
        view_movies()

    elif choice == "3":
        search_movie()

    elif choice == "4":
        delete_movie()

    elif choice == "5":
        save_movies()
        print("Movies saved. Goodbye!")
        break

    else:
        print("Invalid choice.")