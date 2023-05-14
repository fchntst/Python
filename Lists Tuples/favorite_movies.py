# Program with favorite movies 

favorite_movies = ['Cosmos', 'Star wars', 'Alien', 'Space odysey']

new_movie = str(input("Give a new movie: "))
if new_movie in favorite_movies:
    print("is already in the list it did not saved the movie")
else: 
    favorite_movies.append(new_movie)
    print(favorite_movies)
    print('the total movies are: ' + str(len(favorite_movies)))


