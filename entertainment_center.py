# -*- coding: cp950 -*-

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")



avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=_Tkc5pQp_JE")



looper = media.Movie("Looper",
                     "time travel is invented by the year 2074",
                     "http://upload.wikimedia.org/wikipedia/en/0/0a/Looper_poster.jpg",
                     "http://www.youtube.com/watch?v=2iQuhsmtfHw")


source_code = media.Movie("Source code",
                     "Source Code is a 2011 French–American science fiction techno-thriller film directed by Duncan Jones, written by Ben Ripley",
                     "http://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg",
                     "http://www.youtube.com/watch?v=NkTrG-gpIzE")



spiderman_2 = media.Movie("Amazing Spider-Man 2",
                     "The Amazing Spider-Man 2 (released as The Amazing Spider-Man 2: Rise of Electro in some markets)[6] is a 2014 American superhero film featuring the Marvel Comics character Spider-Man",
                     "http://upload.wikimedia.org/wikipedia/en/0/02/The_Amazing_Spiderman_2_poster.jpg",
                     "http://www.youtube.com/watch?v=DlM2CWNTQ84")


red_minibus = media.Movie("The Midnight After",
                     "all people disappear after the red minbus travelled through the lion tunnel",
                     "http://upload.wikimedia.org/wikipedia/zh/6/62/The_Midnight_After_early_movie_poster.jpeg",
                     "http://www.youtube.com/watch?v=xs_oXMovzQI")

movies = [toy_story, avatar, looper, source_code, spiderman_2, red_minibus]
fresh_tomatoes.open_movies_page(movies)

