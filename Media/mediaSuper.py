class Video():
       def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url,duration):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube_url
        self.duration=duration

       def show_trailer(self,movie_wiki):
            return movie_wiki
