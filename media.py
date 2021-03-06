import webbrowser

class Movie():
    """
    Creates a movie object with the variables title, storyline,
    poster_image_url, trailer_youtube_url and a show_trailer method.   
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function opens the youtube link for the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
