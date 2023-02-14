def isIMDB55(movie):
    if movie["imdb"] > 5.5:
        return True


def sublistIMDB55(movies):
    newMovies = []
    for i in movies:
        if isIMDB55(i):
            newMovies.append(i)
    return newMovies


def category(movies, cat):
    catMovies = []
    for i in movies:
        if i["category"] == cat:
            catMovies.append(i)
    return catMovies


def avIMDB(movies):
    IMDBsum = count = 0
    for i in movies:
        IMDBsum += i["imdb"]
        count += 1
    return IMDBsum / count


def IMDBofCategory(movies, cat):
    catMovies = category(movies, cat)
    return avIMDB(catMovies)


movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(movies[3]["name"], "movie has IMDB is above 5.5: ", isIMDB55(movies[3]), "\n")
print("These movies have IMDB above 5.5:\n", sublistIMDB55(movies), "\n")
print("These movies are of Romance category:\n", category(movies, "Romance"), "\n")
print("The average IMDB of movies is: ", avIMDB(movies), "\n")
print("The average IMDB of movies with category Action is: ", IMDBofCategory(movies, "Action"))
