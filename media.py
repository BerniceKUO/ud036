import webbrowser
import mediaSuper
class Movie(mediaSuper.Video):
    #這個是電影的共用類別   
    VALID_RATINGS=["普遍級","保護級","輔導級","限制級"]#不會改變的常數變數名稱要用大寫
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url,duration,movie_ratings):
        mediaSuper.Video.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url,duration)
        self.ratings=movie_ratings;

    #def show_trailer(self):
        #webbrowser.open(self.trailer_youtube_url)
    def show_ratings(self):
        return self.VALID_RATINGS[self.ratings]

class TVShow(mediaSuper.Video):
     #這個是影集的共用類別
     def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url,duration,tv_class,tv_season,tv_episode):
        mediaSuper.Video.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url,duration)
        self.season=tv_season
        self.episode=tv_episode
        self.trailer_youtube_url=trailer_youtube_url
        self.tvclass=tv_class
     def show_trailer(self):
         print("===test===")
         webbrowser.open_new_tab(self.trailer_youtube_url)
     def show_ratings(self):
         return self.tvclass

