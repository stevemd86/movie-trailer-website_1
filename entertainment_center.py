import fresh_tomatoes
import media

# 2001 Space Odyssey
spaceodyssey = media.Movie("2001 Space Odyssey",
                        "Kubrick's best work",
                        "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                        "https://www.youtube.com/watch?v=Z2UWOeBcsJI")

# Gangs of New York
gangs = media.Movie("Gangs of New York",
                     "Scorsese's best work",
                     "http://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",
                     "https://www.youtube.com/watch?v=UYsS_3zdwmA")

# Groundhog Day
groundhogday = media.Movie("Groundhog Day",
                             "Bill Murry's best work",
                             "http://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
                             "https://www.youtube.com/watch?v=tSVeDx9fk60")

# Raiders of the Lost Ark
raiders = media.Movie("Raiders of the Lost Ark",
                          "Harrison Ford's best work",
                          "http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",
                          "https://www.youtube.com/watch?v=XkkzKHCx154")

# Alien
alien = media.Movie("Alien",
                                "Ridley Scott's best work",
                                "http://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                                "https://www.youtube.com/watch?v=LjLamj-b0I8")

# The Shining
shining = media.Movie("The Shining",
                          "Jack Nicholson's best",
                          "http://upload.wikimedia.org/wikipedia/en/2/25/The_Shining_poster.jpg",
                          "https://www.youtube.com/watch?v=1G7Ju035-8U")

# Build website
movies = [spaceodyssey, gangs, groundhogday,
          raiders, alien, shining]

fresh_tomatoes.open_movies_page(movies)