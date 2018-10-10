from movie import Movie
from user import User

user = User("Jose")

my_movie = Movie("The Matrix", "Sci-Fi", False)
watched_movie = Movie("Coraline", "Children's", True)

user.movies.append(my_movie)
user.movies.append(watched_movie)

print(user)
print(user.movies)
print(user.watched_movies())