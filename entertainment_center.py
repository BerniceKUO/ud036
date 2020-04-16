import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story","玩具的友誼與冒險故事"
                      ,"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                      ,"https://www.youtube.com/watch?v=TYNCL2vtEbk&feature=emb_rel_err","1小時60分鐘",0)
avatar=media.Movie("Avatar","人類侵入外星球大搞破壞，外星人反撲的故事"
                   ,"https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
                   ,"https://www.youtube.com/watch?v=-9ceBgWV8io","2小時20分鐘",2)
StrangerThings=media.TVShow("Stranger Things","講述一名年輕男孩忽然失蹤後，一位擁有超能力的年輕女孩幫男孩的朋友尋找男孩的下落，而男孩的哥哥與小鎮警署的警長也各自展開他們的調查。"
                   ,"https://img.zi.org.tw/ddm/2017/09/1506663337-8bccb67b5773b35b8bb7e15e93b8e925.jpg"
                   ,"https://www.youtube.com/watch?v=vkznPsngX0M","每集45分鐘","科幻恐怖","第一季","第一集")
movies_TV=[toy_story,avatar,StrangerThings]
fresh_tomatoes.open_movies_page(movies_TV)

