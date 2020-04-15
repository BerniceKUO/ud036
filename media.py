import webbrowser
class Movie():
    #這個是電影的共用類別   
    VALID_RATINGS=["普遍級","保護級","輔導級","限制級"]#不會改變的常數變數名稱要用大寫
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
class TVShow():
     #這個是影集的共用類別
     def __init__(self,tv_season,tv_episode,tv_station,trailer_youtube_url):
        self.season=tv_season
        self.episode=tv_episode
        self.station=tv_station
        self.trailer_youtube_url=trailer_youtube_url
    
