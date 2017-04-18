import media
import fresh_tomatoes

hidden_figures = media.Movie("Hidden Figures",
                             "Three brilliant African-American women at NASA help the launch of astronaut John Glenn into orbit.",
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",
                             "https://www.youtube.com/watch?v=RK8xHq6dfAo")  
singin_rain = media.Movie("Singin' In The Rain",
                          "A silent film production company and cast make a difficult transition to sound",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/Singing_in_the_rain_poster.jpg",
                          "https://www.youtube.com/watch?v=36QiuRc_3I8")
rear_window = media.Movie("Rear Window",
                          "Sitting in a wheelchair, a photographer spies on courtyard neighbors and sees a murder",
                          "https://upload.wikimedia.org/wikipedia/commons/3/38/Rear_Window_film_poster.jpg",
                          "https://www.youtube.com/watch?v=6kCcZCMYw38")
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
lala_land = media.Movie("La La Land",
                        "Two young people in Los Angeles try to navigate love and careers",
                        "https://upload.wikimedia.org/wikipedia/en/e/e2/La_La_Land_Poster.jpg",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")
casablanca = media.Movie("Casablanca",
                         "A nightclub owner helps an old flame and her husband escape the Germans",
                         "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
                         "https://www.youtube.com/watch?v=BkL9l7qovsE")

movies = [toy_story, hidden_figures, singin_rain, rear_window, lala_land, casablanca]

# This will create the html with all the above movies and display inside a web browser
fresh_tomatoes.open_movies_page(movies)

