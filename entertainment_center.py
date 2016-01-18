import media
import varuns_movies

inception = media.Movie("Inception",
                        "A movie about existencialism",
                        "http://vignette2.wikia.nocookie.net/inception/images/9/9e/Inceptionpromotionalposter.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

#print(inception.storyline)
dark_knight = media.Movie("Dark Knight",
                     "A movie about how insanity and sanity are only one bad day away",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")
#print (dark_knight.storyline)
#dark_knight.show_trailer()
guru = media.Movie("Guru",
                   "A movie about a boy from a small town builds India's largest company to date",
                   "https://upload.wikimedia.org/wikipedia/en/c/c9/Guruposter.JPG",
                   "https://www.youtube.com/watch?v=D1eE-lCKcxI")
fight_club=media.Movie("Fight Club",
                       "A movie about two men with a similar goal",
                       "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                       "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forrest_gump=media.Movie("Forest Gump",
                        "A journey about a mentally challenged person changing the lives of americans",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")

#movies = [inception, dark_knight, guru, fight_club, forrest_gump]
#print (media.Movie.VALID_RATINGS)
#varuns_movies.open_movies_page(movies)
print (media.Movie.__doc__)
