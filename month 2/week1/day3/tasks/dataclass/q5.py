from dataclasses import dataclass

@dataclass
class Movie:
    movie_name: str
    director: str
    rating: float


m1 = Movie("Inception", "Christopher Nolan", 8.8)
m2 = Movie("Inception", "Christopher Nolan", 8.8)

print(m1 == m2)