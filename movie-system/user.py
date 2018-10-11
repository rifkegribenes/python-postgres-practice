from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    def __repr__(self):
        return "<User {}>".format(self.name)


    def add_movie(self, name, genre):
        new_movie = Movie(name, genre, False)
        self.movies.append(new_movie)


    def delete_movie(self, name):
        return list(filter(lambda movie: movie.name != name, self.movies))


    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))


    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))