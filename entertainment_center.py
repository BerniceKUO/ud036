import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story","玩具的友誼與冒險故事"
                      ,"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                      ,"https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar=media.Movie("Avatar","人類侵入外星球大搞破壞，外星人反撲的故事"
                   ,"https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
                   ,"https://www.youtube.com/watch?v=-9ceBgWV8io")
movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)

